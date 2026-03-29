#!/usr/bin/env python3
"""fraction_calc - Exact fraction arithmetic with GCD simplification."""
import sys, json, math

class Frac:
    def __init__(self, num, den=1):
        if den < 0: num, den = -num, -den
        g = math.gcd(abs(num), den)
        self.num = num // g; self.den = den // g
    
    def __repr__(self):
        if self.den == 1: return str(self.num)
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):
        return Frac(self.num*other.den + other.num*self.den, self.den*other.den)
    
    def __sub__(self, other):
        return Frac(self.num*other.den - other.num*self.den, self.den*other.den)
    
    def __mul__(self, other):
        return Frac(self.num*other.num, self.den*other.den)
    
    def __truediv__(self, other):
        if other.num == 0: raise ZeroDivisionError
        return Frac(self.num*other.den, self.den*other.num)
    
    def __pow__(self, n):
        if n < 0: return Frac(self.den**(-n), self.num**(-n))
        return Frac(self.num**n, self.den**n)
    
    def __eq__(self, other): return self.num == other.num and self.den == other.den
    def __lt__(self, other): return self.num * other.den < other.num * self.den
    
    def to_float(self): return self.num / self.den
    
    def to_continued_fraction(self):
        cf = []; a, b = self.num, self.den
        while b:
            q, r = divmod(a, b)
            cf.append(q); a, b = b, r
        return cf
    
    @staticmethod
    def from_continued_fraction(cf):
        if not cf: return Frac(0)
        num, den = cf[-1], 1
        for i in range(len(cf)-2, -1, -1):
            num, den = cf[i]*num + den, num
        return Frac(num, den)

def main():
    print("Fraction calculator demo\n")
    a = Frac(1, 3); b = Frac(1, 6)
    print(f"  {a} + {b} = {a+b}")
    print(f"  {a} - {b} = {a-b}")
    print(f"  {a} * {b} = {a*b}")
    print(f"  {a} / {b} = {a/b}")
    print(f"  {a}^3 = {a**3}")
    # Harmonic sum
    h = Frac(0)
    for i in range(1, 11): h = h + Frac(1, i)
    print(f"  H(10) = {h} ≈ {h.to_float():.6f}")
    # Continued fractions
    pi_approx = Frac(355, 113)
    cf = pi_approx.to_continued_fraction()
    print(f"  355/113 CF: {cf}")
    back = Frac.from_continued_fraction(cf)
    print(f"  Reconstructed: {back}")

if __name__ == "__main__":
    main()
