def prod_non_zero_diag(x):
    n = min(len(x), len(x[0]))
    res = 1
    for i in range(n):
        if x[i][i] != 0:
            res *= x[i][i]

    return res 


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    if len(x) != len(y): return False
    for i in range(len(x)):
        if x[i] != y[i]: return False
    return True


def max_after_zero(x):
    mx = 0
    for i in range(1, len(x)):
      if x[i - 1] == 0:
        mx = max(mx, x[i])
    return mx


def convert_image(img, coefs):
    a = [[0] * len(img[0]) for y in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                t1 = img[i][j][k]
                t2 = coefs[k]
                a[i][j] += t1 * t2

    return a



def run_length_encoding(x):
    x.sort()
    last = x[0]
    cnt = 1
    ans1 = []
    ans2 = []
    for i in range(1, len(x)):
      if last == x[i]:
        cnt += 1
      else :
        ans1.append(last)
        ans2.append(cnt)
        cnt = 1
        last = x[i]
    ans1.append(last)
    ans2.append(cnt)
    return ans1, ans2


def pairwise_distance(x, y):
  n = len(x)
  A = [[0] * n for j in range(n)]
  for i in range(n):
    for j in range(n):
      A[i][j] = ((x[i][0] - y[j][0])**2 + (x[i][1] - y[j][1])**2) ** 0.5
  return A





