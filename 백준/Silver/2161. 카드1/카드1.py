from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
myque = deque(range(1, N+1))

while len(myque) > 1:
    print(myque.popleft(), end = ' ')
    myque.append(myque.popleft())
print(myque[0])