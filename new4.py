# -*- coding:utf-8 -*-
import sys
import math
lines=[]
try:zx
    while True:
        line=sys.stdin.readline().strip()
        a=list(map(int,line.split(' ')))
        lines.append(a)
        if line==" ":
            break
except:
    pass
count=0
for i in lines[1][:lines[0][0]-2]:
    shaogang=[]
    shaogang.append(lines[1][lines[1].index(i)+1])
    count+=1
    for j in lines[1][lines[1].index(i)+2:]:
        if max(i,j)<max(shaogang):
            break
        else:
            count+=1
            shaogang.append(j)
count+=1
print count