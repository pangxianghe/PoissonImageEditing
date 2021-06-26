import numpy as np
from scipy.sparse import linalg
from scipy.sparse import lil_matrix


# https://en.wikipedia.org/wiki/Discrete_Poisson_equation
# src, tgt, msk should be the same shape


def mask_indices(mask):
    #  return a list containing the ROI points
    nonzero = np.nonzero(mask)
    return list(zip(nonzero[0], nonzero[1]))


def get_surrounding(index):
    i, j = index
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def poisson_sparse_matrix(points):
    # According to Discrete_Poisson_equation, return A matrix
    N = len(points)
    A = lil_matrix((N, N))
    for i, index in enumerate(points):
        A[i, i] = 4
        for x in get_surrounding(index):
            if x not in points:
                continue
            j = points.index(x)
            A[i, j] = -1
    return A


def laplacian(source, index):
    # compute the divergence of the given points
    i, j = index
    val = (4 * source[i, j]) - (1 * source[i + 1, j]) - (1 * source[i - 1, j]) - (1 * source[i, j + 1]) - (
                1 * source[i, j - 1])
    return val


def gradient(source, index):
    # compute the gradient of the given points
    i, j = index
    val = (1 * source[i + 1, j]) - (1 * source[i - 1, j]) + (1 * source[i, j + 1]) - (
                1 * source[i, j - 1])
    return val


def on_edge(index, mask):
    # a point is inside the mask and its neighbor is outside the mask
    if not in_omega(index, mask):
        return False
    for pt in get_surrounding(index):
        if not in_omega(pt, mask):
            return True
    return False


def in_omega(index, mask):
    return mask[index] == 1


def process(source, target, mask, flag=0):
    """
    process one channel of the image
    :param flag: SeamlessClone, MixingGradients
    :param source:(N, M) source image
    :param target:(N, M) target image
    :param mask:(N, M) mask where the ROI value = 1 else = 0
    :return:one channel of the processed image
    """
    indices = mask_indices(mask)
    N = len(indices)
    A = poisson_sparse_matrix(indices)
    b = np.zeros(N)
    for i, index in enumerate(indices):

        if flag == 0:
            # SeamlessClone
            mixer = source
        else:
            # MixingGradients
            if gradient(source, index) > gradient(target, index):
                mixer = source
            else:
                mixer = target

        b[i] = laplacian(mixer, index)
        if on_edge(index, mask):
            for pt in get_surrounding(index):
                if not in_omega(pt, mask):
                    b[i] += target[pt]
    x = linalg.cg(A, b)  # shape(array, 0)
    target_new = np.copy(target).astype(int)
    for i, index in enumerate(indices):
        target_new[index] = x[0][i]
    return target_new


def naive_clone(source, target, mask):
    return target * (1.0 - mask) + source * mask
