#-*- coding:utf-8 -*-
import math
n=input()
aa=[]
bb=[]
count=0
for i in range(1,n+1):
    a=i
    aa=str(a)
    suma=0
    for j in range(len(aa)):
        suma=suma+int(aa[j-1])    
    b=bin(i)
    bb=str(b)
    sumb=0
    for k in range(len(bb)-2):
        sumb=sumb+int(bb[k+2])

    if suma==sumb:
        count+=1
print count