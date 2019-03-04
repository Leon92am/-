#-*- coding: utf-8 -*-
import sys
import math
import fractions
def f(n,x):
    #n为待转换的十进制数，x为多少进制
    b=[]
    while True:
        s=n//x#商
        y=n%x#余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    return b

def divisor(m,n):
    while (m%n>0):
        c=m%n
        m=n
        n=c
    return n


A=map(int,raw_input().split(" "))
B=[]
for i in A:
    s=0
    if i>=2:
        for j in range(2,i):
            s=s+sum(f(i,j))
        fenzi=s/(divisor(s,i-2))
        fenmu=(i-2)/(divisor(s,i-2))
        B.append(str(fenzi)+'/'+str(fenmu))
    else:
        B.append(str(1))
for i in B:
    print i


