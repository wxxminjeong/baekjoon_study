import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
mydeque = deque()

for i in range(N):
    while mydeque and mydeque[-1][1] > A[i]:
        mydeque.pop()
    mydeque.append([i,A[i]])
    if i - mydeque[0][0] >= L:
        mydeque.popleft()
    print(mydeque[0][1], end = ' ')
