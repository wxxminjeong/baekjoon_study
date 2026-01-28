import sys
input = sys.stdin.readline

N = int(input())
mylist = []
for i in range(N):
    mylist.append(int(input()))

for i in range(N-1):
    for j in range(N-1-i):
        if mylist[j] > mylist[j+1]:
            temp = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp

for i in range(N):
    print(mylist[i])
