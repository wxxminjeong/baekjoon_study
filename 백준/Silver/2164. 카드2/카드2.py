from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
myque = deque(range(1, N+1))

while len(myque) > 1:
    myque.popleft()
    myque.append(myque.popleft())

print(myque[0])