# construct suffix array of a string
# O(nlogn)
# 2018-10-10
# by zhangzhi

from functools import cmp_to_key


class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.sa = []
        self.height = []
        self.build()

    def build(self):
        s = self.s
        n = len(s)
        sa = self.sa
        rk = [0] * n
        height = self.height
        for i in range(n):
            sa.append(i)
            rk[i] = ord(s[i])
        k = 1
        while k < n:
            def cmp(x, y):
                if rk[x] != rk[y]:
                    return rk[x] - rk[y]
                else:
                    rx = rk[x + k] if x + k < n else -1
                    ry = rk[y + k] if y + k < n else -1
                    return rx - ry
            sa.sort(key=cmp_to_key(cmp))
            trk = [0] * n
            trk[sa[0]] = 0
            for i in range(1, n):
                trk[sa[i]] = trk[sa[i - 1]]
                if cmp(sa[i - 1], sa[i]) < 0:
                    trk[sa[i]] += 1
            rk = trk
            k *= 2
        k = 0
        for i in range(n):
            if k > 0:
                k -= 1
            j = sa[rk[i] - 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            height.append(k)

    def get_sa(self):
        return self.sa

    def get_height(self):
        return self.height

print(SuffixArray("test#").get_sa())
    