from collections import Iterable
import sys
line=sys.stdin.readline().strip()
print isinstance(map(int,line.split(' ')),Iterable)