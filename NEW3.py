# -*- coding: utf-8 -*-
import math
import sys
lines=[]
try:
    while True:
        line=sys.stdin.readline().strip()
        a=list(map(int,line.split(' ')))
        lines.append(a)
        if line =='':
            break
except:
    pass
print lines
S=lines[0]
A=lines[1]
B=lines[2]
AA=A[:S[0]]
BB=B[:S[1]]
C=AA+BB
C_sort=sorted(C)
newc=[]
for i in C_sort:
    if i not in newc:
        newc.append(i)
print(" ".join(str(x) for x in newc))#以空格作为连接，连接序列中的元素生成一个字符串




