#coding:utf-8
import sys
import numpy as  np
Numbers=[123, 895, 119, 1037]
Matrix = [
  [1, 2, 3, 4],
  [3, 5, 9, 8],
  [8, 0, 3, 7],
  [6, 1, 9, 2]
]
Matrix=np.array(Matrix)
[m,n]=Matrix.shape

def isnear(x,y,M):
    target={}#匹配到的x的坐标作为键，y的坐标作为值
    for i in range(m):
        for j in range(n):
            if M[i,j]==x:#搜索四邻域
                target[i,j]=[]
                try:
                    if M[i-1,j]==y:
                        target[i, j].append((i-1,j))
                except:
                    pass
                try:
                    if M[i+1,j] == y:
                        target[i, j].append((i+1, j))
                except:
                    pass
                try:
                    if M[i,j-1] == y:
                        target[i, j].append((i, j-1))
                except:
                    pass
                try:
                    if M[i,j+1] == y:
                        target[i, j].append((i,j+1))
                except:
                    pass
    return target



#def find_integers(numbers,Matrix):
for i in Numbers:
    print i
    for j in range(len(str(i))-1):
        x=int(str(i)[j])
        y=int(str(i)[j+1])
        used = []
        T=isnear(x,y,Matrix)
        if len(T)==0:
            print "没有匹配到x"
        else:
            for k in T:
                xindex=k
                yindex=T[k]
                if len(yindex)!=0:
                    for z in yindex:
                        if z not in used:
                            used.append(z)

