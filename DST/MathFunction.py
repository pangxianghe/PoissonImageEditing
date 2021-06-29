import numpy as np
import scipy.fftpack


def DST(x):
    return scipy.fftpack.dst(x, type=1, axis=0) / 2.0
    #  function of scipy is two times of the standard form
    #  type 1 has no bias


def IDST(X):
    x = np.real(scipy.fftpack.idst(X, type=1, axis=0))
    return x / (X.shape[0] + 1.0)  # IDST = DST / N + 1


def genGradient(im):
    rows, cols = im.shape
    dx = np.zeros((rows, cols), dtype=np.float32)
    dy = np.zeros((rows, cols), dtype=np.float32)
    for i in range(rows - 1):
        for j in range(cols - 1):
            dx[i, j] = im[i, j + 1] - im[i, j]
            dy[i, j] = im[i + 1, j] - im[i, j]
    return dx, dy


def genLaplacian(dx, dy):
    rows, cols = dx.shape
    lapx = np.zeros((rows, cols), dtype=np.float32)
    lapy = np.zeros((rows, cols), dtype=np.float32)
    for i in range(1, rows):
        for j in range(1, cols):
            lapx[i, j] = dx[i, j] - dx[i, j - 1]
            lapy[i, j] = dy[i, j] - dy[i - 1, j]
    return lapx + lapy


def solvePoisson(lap, img):
    """
    Solve the Poisson Function
    :param lap: Right side of the poisson equation
    :param img: ROI of the target image
    :return: Solution of the equation
    """
    # https://elonen.iki.fi/code/misc-notes/neumann-cosine/
    # here Neumann boundary is implemented, rather than the Dirichlet boundary
    # thus compute (lap - img)
    img = img.astype('float32')
    rows, cols = img.shape
    img[1:-1, 1:-1] = 0

    L_bp = np.zeros_like(lap)
    L_bp[1:-1, 1:-1] = -4 * img[1:-1, 1:-1] \
                       + img[1:-1, 2:] + img[1:-1, 0:-2] \
                       + img[2:, 1:-1] + img[0:-2, 1:-1]
    L = (lap - L_bp)[1:-1, 1:-1]
    L_dst = DST(DST(L).T).T  # to compute 2D-DST, compute 1-D DST in row and column sequentially

    [xx, yy] = np.meshgrid(np.arange(1, cols - 1), np.arange(1, rows - 1))
    D = (2 * np.cos(np.pi * xx / (cols - 1)) - 2) + (2 * np.cos(np.pi * yy / (rows - 1)) - 2)
    L_dst = L_dst / D

    img_interior = IDST(IDST(L_dst).T).T
    img = img.copy()
    img[1:-1, 1:-1] = img_interior

    return img
