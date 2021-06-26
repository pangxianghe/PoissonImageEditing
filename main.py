import cv2
import numpy as np
import poisson

src_path = './images/input/4/source.png'
msk_path = './images/input/4/mask.png'
tgt_path = './images/input/4/target.png'
out_path = './images/output/4/result_MixingGradient1.png'

src = cv2.imread(src_path, cv2.IMREAD_COLOR)
msk = cv2.imread(msk_path, cv2.IMREAD_GRAYSCALE)
tgt = cv2.imread(tgt_path, cv2.IMREAD_COLOR)

if src.shape != tgt.shape:
    # when src.shape!=tgt.shape, use h and w to locate the center of ROI
    h = 131
    w = 141
    trans = np.float32([[1, 0, int(w - src.shape[1] / 2)], [0, 1, int(h - src.shape[0] / 2)]])
    src = cv2.warpAffine(src, trans, (tgt.shape[1], tgt.shape[0]))
    msk = cv2.warpAffine(msk, trans, (tgt.shape[1], tgt.shape[0]))


if __name__ == '__main__':
    msk = msk.astype(np.float64) / 255
    msk[msk != 1] = 0
    result_stack = [poisson.process(src[:, :, i], tgt[:, :, i], msk, flag=1) for i in range(3)]
    # result_stack = [poisson.naive_clone(src[:, :, i], tgt[:, :, i], msk) for i in range(3)]
    result = cv2.merge(result_stack)

    cv2.imwrite(out_path, result)
