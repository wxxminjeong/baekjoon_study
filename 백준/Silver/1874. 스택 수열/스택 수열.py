import sys
input = sys.stdin.readline

n = int(input())
target = []
for _ in range(n):
    target.append(int(input()))
my_stack = []
num = 1
answer = []
is_n = True

for t in target:
    if t >= num:
        while t >= num:
            my_stack.append(num)
            num += 1
            answer.append('+')
        my_stack.pop()
        answer.append('-')
        
    elif t < num:
        if t < my_stack[-1]:
            print('NO')
            is_n = False
            break
        my_stack.pop()
        answer.append('-')
    
if is_n:
    for i in answer:
        print(i)
    