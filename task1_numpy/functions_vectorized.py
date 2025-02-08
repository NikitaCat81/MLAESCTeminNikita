import numpy as np


def prod_non_zero_diag(ms):
    a = ms.diagonal(0)
    a = np.where(a != 0, a, 1)
    return np.prod(a)


def are_multisets_equal(ms_1, ms_2):
    ms_1_n, ms_1_c = np.unique(ms_1, return_counts=True)
    ms_2_n, ms_2_c = np.unique(ms_2, return_counts=True)
    if(np.shape(ms_1_n) != np.shape(ms_2_n)):
        return False
    if(np.any(ms_1_n != ms_2_n) or np.any(ms_1_c !=ms_2_c)):
        return False
    return True


def max_after_zero(ms):
    a = np.ones((1))
    a = np.hstack((a, ms))
    i = a == 0
    return np.max(ms)


def convert_image(img, coeff):
    return np.sum(img * coeff, axis=-1)


def run_length_encoding(ms):
    a = np.hstack((np.ones(1), ms[:- 1]))
    f = ms != a
    f[0] = True
    i_1 = np.arange(np.size(ms))[f]
    i_2 = np.hstack((i_1[1:], np.array([np.size(ms)])))
    return ms[f], i_2 - i_1


def pairwise_distance(ms1, ms2):
    return np.sqrt(np.sum((ms1[:, np.newaxis] - ms2) ** 2, axis=-1))