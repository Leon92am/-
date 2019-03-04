#coding:utf-8
#以升序为例
import sys

def InsertSORT(array1):
    gap=len(array1)
    while gap>1:
        gap=gap//2
        for i in range(gap,len(array1)):#从第一个增量位置对应的元素开始，一次进行比较
            while(i>=gap and array1[i-gap]>array1[i]):
                array1[i],array1[j]=array1[j],array1[i]
                i-=gap
    return array1


a=InsertSORT([1,5,73,6,3])
print a
