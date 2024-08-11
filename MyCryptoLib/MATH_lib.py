import gmpy2
import functools
from Crypto.Util.number import *

class MATH:
    @staticmethod
    def crt(a, m):
        '''
        Input: [a_1, ... a_n], [m_1, ..., m_n]
            x = a_1 (mod m_1)
            x = a_2 (mod m_2)
            ...
            x = a_n (mod m_n)
        Output: x
        '''
        prod, total = functools.reduce(lambda x, y: x * y, m), 0
        for ai, mi in zip(a, m):
            Mi = prod // mi
            total += ai * Mi * (gmpy2.gcdext(Mi, mi)[1] % mi)
        return total % prod
    
    @staticmethod
    def gcd(a, b):
        while b != 0:
            t = a % b
            a = b
            b = t
        return a