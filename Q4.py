#coding:utf-8
import sys

lines=[]
try:
    while True:
        line = sys.stdin.readline().strip()
        a=list(map(int,line.split(' ')))
        lines.append(a)
        if line==" ":
            break
except:
    pass
#求最小公共区间
start=0
end=100000
for i in lines:
    if min(i)>start:
        start=min(i)
    if max(i)<end:
        end=max(i)
print start,end

