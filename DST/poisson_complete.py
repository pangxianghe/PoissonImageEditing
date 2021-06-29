from pro_post import *
from MathFunction import *


class Poisson:
    def __init__(self, offset, src_img, src_mask, dst_img):
        self.offset = offset
        self.src_img = src_img
        self.src_mask = src_mask
        self.dst_img = dst_img
        self.tl, self.br = getRect(self.src_mask)
        self.top_img = self.src_img[self.tl[0]:self.br[0], self.tl[1]:self.br[1], :]
        self.msk = self.src_mask[self.tl[0]:self.br[0], self.tl[1]:self.br[1], :]

        if self.dst_img is not None:
            self._tl, self._br = genDstRect(self.tl, self.br, self.offset)
            self.ground_img = self.dst_img[self._tl[0]:self._br[0], self._tl[1]:self._br[1], :]

    def process(self, proc_type):
        if proc_type == 'SeamlessClone':
            self.patch = self.SeamlessClone()
        elif proc_type == 'MixingGradientClone':
            self.patch = self.MixingGradientClone()
        elif proc_type == 'TextureFlattening':
            self.patch = self.TextureFlattening()
        elif proc_type == 'Local_ill_changes':
            self.patch = self.Local_ill_changes()
        elif proc_type == 'Local_color_changes':
            self.patch = self.Local_color_changes()

        if self.dst_img is not None:
            res = genRes(self.dst_img, self.patch, self._tl)
        else:
            res = genRes(self.src_img, self.patch, self.tl)

        # naive_res = genNaiveRes(self.dst_img, self.top_img, self.msk, self._tl)
        return res

    def SeamlessClone(self):
        rows, cols, dims = self.top_img.shape

        im_top = self.top_img.copy().astype('float32')
        im_ground = self.ground_img.copy().astype('float32')
        im_res = np.zeros((rows, cols, dims), dtype=np.float32)

        for dim in range(dims):
            dx_t, dy_t = genGradient(im_top[:, :, dim])
            dx_g, dy_g = genGradient(im_ground[:, :, dim])
            dx, dy = dx_g.copy(), dy_g.copy()

            msk_region = np.where(self.msk[:, :, dim] != 0)
            dx[msk_region] = dx_t[msk_region]
            dy[msk_region] = dy_t[msk_region]

            lap = genLaplacian(dx, dy)
            im_res[:, :, dim] = np.clip(solvePoisson(lap, im_ground[:, :, dim]), 0, 255)

        return im_res.astype('uint8')

    def MixingGradientClone(self):
        rows, cols, dims = self.top_img.shape

        im_top = self.top_img.copy().astype('float32')
        im_ground = self.ground_img.copy().astype('float32')
        im_res = np.zeros((rows, cols, dims), dtype=np.float32)

        for dim in range(dims):
            dx_t, dy_t = genGradient(im_top[:, :, dim])
            dx_g, dy_g = genGradient(im_ground[:, :, dim])
            dx, dy = dx_g.copy(), dy_g.copy()

            for i in range(rows):
                for j in range(cols):
                    if self.msk[i, j, dim] != 0:
                        if abs(dx[i, j]) + abs(dy[i, j]) < abs(dx_t[i, j]) + abs(dy_t[i, j]):
                            dx[i, j], dy[i, j] = dx_t[i, j], dy_t[i, j]

            lap = genLaplacian(dx, dy)
            im_res[:, :, dim] = np.clip(solvePoisson(lap, im_ground[:, :, dim]), 0, 255)

        return im_res.astype('uint8')

    def TextureFlattening(self):
        rows, cols, dims = self.top_img.shape

        im1 = self.top_img.copy().astype('float32')
        im_res = np.zeros((rows, cols, dims), dtype=np.float32)
        edge_map = genEdgeMap(self.top_img)

        for dim in range(dims):
            [dx, dy] = genGradient(im1[:, :, dim])

            for i in range(rows):
                for j in range(cols):
                    if self.msk[i, j, dim] != 0:
                        dx[i, j] = dx[i, j] * edge_map[i, j]
                        dy[i, j] = dy[i, j] * edge_map[i, j]

            lap = genLaplacian(dx, dy)
            im_res[:, :, dim] = np.clip(solvePoisson(lap, im1[:, :, dim]), 0, 255)
        return im_res.astype('uint8')

    def Local_ill_changes(self):
        rows, cols, dims = self.top_img.shape

        im1 = self.top_img.copy().astype('float32')
        im_res = np.zeros((rows, cols, dims), dtype=np.float32)

        for dim in range(dims):
            [dx, dy] = genGradient(im1[:, :, dim])
            d_sum, d_avg = 0, 0
            for i in range(rows):
                for j in range(cols):
                    d_sum = d_sum + dx[i, j] + dy[i, j]
            d_avg = abs(d_sum * 0.2 / rows / cols)

            for i in range(rows):
                for j in range(cols):
                    if self.msk[i, j, dim] != 0:
                        if dx[i, j] != 0:
                            dx[i, j] = dx[i, j] * (abs(dx[i, j]) ** -0.2) * (d_avg ** 0.2)
                        if dy[i, j] != 0:
                            dy[i, j] = dy[i, j] * (abs(dy[i, j]) ** -0.2) * (d_avg ** 0.2)

            lap = genLaplacian(dx, dy)
            im_res[:, :, dim] = np.clip(solvePoisson(lap, im1[:, :, dim]), 0, 255)
        return im_res.astype('uint8')

    def Local_color_changes(self):
        rows, cols, dims = self.top_img.shape

        im_top = self.top_img.copy().astype('float32')
        im_ground = self.ground_img.copy().astype('float32')
        im_res = np.zeros((rows, cols, dims), dtype=np.float32)

        for dim in range(dims):
            dx_t, dy_t = genGradient(im_top[:, :, dim])

            if dim == 0:    # blue
                alpha = 0.5
            elif dim == 1:  # green
                alpha = 0.5
            else:           # red
                alpha = 1.5
            dx_t *= alpha
            dy_t *= alpha

            dx_g, dy_g = genGradient(im_ground[:, :, dim])
            dx, dy = dx_g.copy(), dy_g.copy()

            msk_region = np.where(self.msk[:, :, dim] != 0)
            dx[msk_region] = dx_t[msk_region]
            dy[msk_region] = dy_t[msk_region]

            lap = genLaplacian(dx, dy)
            im_res[:, :, dim] = np.clip(solvePoisson(lap, im_ground[:, :, dim]), 0, 255)

        return im_res.astype('uint8')
