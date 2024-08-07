import gmpy2
from Crypto.Util.number import *
from math import gcd
from wiener import *
from MATH_lib import * 

class RSA:
    @staticmethod
    def RSAencrypt(pbits: int, qbits:int, e:int, msg:bytes):
        m = bytes_to_long(msg)
        p=getPrime(pbits)
        q=getPrime(qbits)
        n=p*q
        c= pow(m,e,n)
        print("n= ", n)
        # print("p= ", p)
        # print("q= ", q)
        print("e= ", e)
        print("c= ", c)

    @staticmethod
    def RSAdecrypt(n: int, p: int, q: int, e: int, c: int) -> bytes:
        n=p*q
        phi = (q - 1) * (p - 1)
        d = inverse(e , phi)
        return long_to_bytes(pow(c , d , n))
    
    @staticmethod
    def small_e(c: int, e:int) -> bytes:
        m = iroot(c, e)[0]
        return long_to_bytes(m)

    @staticmethod
    def broadcast_attack(c_list: list, n_list: list) -> bytes:
        '''
        n0 = 
        c0 = 
        n1 = 
        c1 = 
        n2 = 
        c2 = 
        RSA.broadcast([c0, c1, c2], [n0, n1, n2])
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
        RSA.Common_Factor(n1, n2, c, e)
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
        p, q = RSA.wiener(n, e)
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




