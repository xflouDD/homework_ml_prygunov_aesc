import numpy as np


def prod_non_zero_diag(x):
    d = np.array(np.diag(x))
    res = np.prod(d, where = (d != 0))
    return res

def are_multisets_equal(x, y):
    np.sort(x)
    np.sort(y)
    res = np.array_equal(x, y)
    return res

def max_after_zero(x):
    return np.max(x[1:][np.nonzero(x[:-1] == 0)])


def convert_image(img, coefs):
    return np.dot(img[...,:3], coefs)


def run_length_encoding(x):
  y = x[1:] != x[:-1]
  i = np.append(np.where(y), len(x) - 1)
  z = np.diff(np.append(-1, i))
  return x[i], z


def pairwise_distance(x, y):
    n = len(x)
    m = len(y)
    x = np.repeat(x, m, axis = 0)
    x.reshape((n * 2, m))
    y = np.tile(y, (n, 1))
    y.reshape((2 * n, m))
    x -= y
    x = x ** 2
    return np.vectorize(np.sqrt)(np.dot(x, np.array([1, 1])))