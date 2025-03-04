def prod_non_zero_diag(ms):
    res = 1
    for i in range(min(len(ms), len(ms[0]))):
        if(ms[i][i] != 0):
            res *= ms[i][i]
    return res


def are_multisets_equal(ms_1, ms_2):
    if(len(ms_1) != len(ms_2)):
        return False
    ms_1.sort()
    ms_2.sort()
    for i in range(len(ms_1)):
        if(ms_1[i] != ms_2[i]):
            return False
    return True


def max_after_zero(ms):
    a = list()
    for i in range(1, len(ms)):
        if((ms[i - 1] == 0).any):
            a.append(ms[i])
    return max(a)


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(ms):
    a = [ms[0]]
    b = list()
    k = 1
    for i in range(1, len(ms)):
        if(ms[i - 1] == ms[i]):
            k = k + 1
        else:
            a.append(ms[i])
            b.append(k)
            k = 1
    b.append(k)
    return a, b


def pairwise_distance(ms1, ms2):
    res = list()
    for i in range(len(ms1)):
        a = list()
        for j in range(len(ms2)):
            b = 0
            for k in range(len(ms1[0])):
                b += (ms1[i][k] - ms2[j][k]) ** 2
            a.append(math.sqrt(b))
        res.append(a)
    return res
