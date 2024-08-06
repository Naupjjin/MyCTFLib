import gmpy2
import functools
from Crypto.Util.number import *
from math import gcd
from wiener import *

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
    

class RSA:
    @staticmethod
    def RSAdecrypt(n: int, p: int, q: int, e: int, c: int) -> bytes:
        n=p*q
        phi = (q - 1) * (p - 1)
        d = inverse(e , phi)
        return long_to_bytes(pow(c , d , n))
    
    @staticmethod
    def broadcast_attack(c_list: list, n_list: list) -> bytes:
        '''
        n0 = 
        c0 = 
        n1 = 
        c1 = 
        n2 = 
        c2 = 
        broadcast([c0, c1, c2], [n0, n1, n2])
        '''
        c = MATH.crt(c_list, n_list)
        m, _ = gmpy2.iroot(c, 3)
        return long_to_bytes(m)

    @staticmethod
    def Common_Factor(n1: int, n2: int, c: int, e:int)-> bytes:
        '''
        n1 =
        n2 =
        c  =
        e  =
        Common_Factor(n1, n2, c, e)
        '''
        n = n1
        p = gcd(n1, n2) 
        q = n // p
        d = inverse(e, (p - 1) * (q - 1))
        m = pow(c, d, n)
        return long_to_bytes(m)
    
    @staticmethod
    def Common_Modulus(n: int, c1: int, c2: int, e1: int, e2: int)-> bytes:
        _, s1, s2 = gmpy2.gcdext(e1, e2)
        m = pow(c1, s1, n) * pow(c2, s2, n) % n
        return long_to_bytes(m)
    
    @staticmethod
    def wiener(n: int, e: int) -> tuple:
        '''
        p, q = wiener(n, e)
        d = inverse(e, (p - 1) * (q - 1))
        m = pow(c, d, n)
        '''
        kd = wiener_attack_func.convergents(wiener_attack_func.cf_expansion(e, n))
        for i, (k, d) in enumerate(kd):
            if k == 0:
                continue
            phi = (e * d - 1) // k
            roots = wiener_attack_func.solve(1, phi - n - 1, n)
            if len(roots) == 2:
                p, q = roots
                if p * q == n:
                    return (p, q)





