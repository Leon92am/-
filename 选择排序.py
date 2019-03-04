#coding:utf-8
#以升序为例
import sys
def selectSORT(array1):
    maxarray=[]
    for i in range(len(array1)):
        maxarray.append(max(array1))
        array1.pop(array1.index(max(array1)))
    maxarray=list(reversed(maxarray))
    return maxarray
a=selectSORT([1,5,73,6,3])
print a


