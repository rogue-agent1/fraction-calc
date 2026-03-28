#!/usr/bin/env python3
"""Fraction calculator — exact rational arithmetic."""
import sys, math
class Frac:
    def __init__(self, n, d=1):
        if d<0: n,d=-n,-d
        g=math.gcd(abs(n),d); self.n=n//g; self.d=d//g
    def __add__(s,o): return Frac(s.n*o.d+o.n*s.d, s.d*o.d)
    def __sub__(s,o): return Frac(s.n*o.d-o.n*s.d, s.d*o.d)
    def __mul__(s,o): return Frac(s.n*o.n, s.d*o.d)
    def __truediv__(s,o): return Frac(s.n*o.d, s.d*o.n)
    def __repr__(s): return f"{s.n}/{s.d}" if s.d!=1 else str(s.n)
    def decimal(s): return s.n/s.d
def parse(s):
    if "/" in s: n,d=s.split("/"); return Frac(int(n),int(d))
    return Frac(int(s))
def cli():
    if len(sys.argv)<4: print("Usage: fraction_calc A op B  (e.g. 1/3 + 1/6)"); sys.exit(1)
    a,op,b=parse(sys.argv[1]),sys.argv[2],parse(sys.argv[3])
    r={"+":a+b,"-":a-b,"*":a*b,"/":a/b}.get(op)
    print(f"  {a} {op} {b} = {r} ({r.decimal():.6f})")
if __name__=="__main__": cli()
