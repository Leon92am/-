#coding:utf-8
#以升序为例
import sys
def InsertSORT(array1):
    for i in range(len(array1)):
        for j in range(i):
            if array1[j]>array1[i]:
                array1.insert(j,array1.pop(i))
                break
    return array1
a=InsertSORT([1,5,73,6,3])
print a