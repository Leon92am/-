#coding:utf-8
#以升序为例
def maopaoSORT(array):
    for i in range(len(array)-1,-1,-1):#每次不需要对后面的元素进行比较，因为一趟排序下来，最后的元素一定是最大的
        swap=0
        for j in range(i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swap+=1
        if swap==0:
            return array
        break
    return array


a=maopaoSORT([30,50,57,77,62,78,94,80,84])
print a

# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(i, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return array

# a=bubble_sort([30,50,57,77,62,78,94,80,84])
# print a

