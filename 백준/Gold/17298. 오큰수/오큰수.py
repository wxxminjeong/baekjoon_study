import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

NGE = [-1] * N
mystack = []

for i in range(N):
    while mystack and A[mystack[-1]] < A[i]:  # 스택이 비어있지 않고 인덱스가 top인 A가 인덱스가 i인 A 보다 작을 경우
        NGE[mystack.pop()] = A[i]
    mystack.append(i)

for answer in NGE:
    print(str(answer), end=" ")