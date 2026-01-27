import sys
import heapq
input = sys.stdin.readline

N = int(input())
myque = []

for i in range(N):
    x = int(input())
    if x == 0:
        if not myque:
            print('0')
        else:
            print(heapq.heappop(myque)[1])
    else:
        heapq.heappush(myque, (abs(x),x))