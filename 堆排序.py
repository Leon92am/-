#coding:utf-8
#以升序为例，大根堆
#首先调整某一个根节点及其子树为大根堆
def max_heapify(heap,heapsize,root):
    leftchild=2*root+1
    rightchild=leftchild+1
    larger=root
    if leftchild<heapsize and heap[leftchild]>heap[larger]:
        larger=leftchild
    if rightchild<heapsize and heap[rightchild]>heap[larger]:
        larger=rightchild
    if larger!=root:
        heap[larger],heap[root]=heap[root],heap[larger]
        max_heapify(heap,heapsize,larger)

def build_heap(heap):#构造大根堆
    heapsize=len(heap)
    for i in range((heapsize-2)//2,-1-1):
        max_heapify(heap,heapsize, i)
    return heap

def heapsort(heap):#交换前后的值
    build_heap(heap)
    for i in range(len(heap)-1,-1-1):
        heap[0],heap[i]=heap[i],heap[0]
        max_heapify(heap, i, 0)
    return heap

a=heapsort([30,50,57,77,62,78,94,80,84])
print a













