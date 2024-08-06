import gmpy2

class wiener_attack_func:
    @staticmethod
    def cf_expansion(n, d):
        q, r = n // d, n % d
        e = [q]
        while r != 0:
            n, d = d, r
            q, r = n // d, n % d
            e.append(q)
        return e

    @staticmethod
    def convergents(e):
        n, d = [], []
        for i in range(len(e)):
            if i == 0:
                ni, di = e[i], 1
            elif i == 1:
                ni, di = e[i] * e[i-1] + 1, e[i]
            else:
                ni, di = e[i] * n[i-1] + n[i-2], e[i] * d[i-1] + d[i-2]
            n.append(ni)
            d.append(di)
            yield (ni, di)

    @staticmethod
    def solve(a, b, c):
        k = b * b - 4 * a * c
        if k < 0:
            return []
        sk, complete = gmpy2.iroot(k, 2)
        if not complete:
            return []
        return [int((-b + sk) // (2 * a)), int((-b - sk) // (2 * a))]