N, M = map(int, input().split())

mylist = list(map(int, input().split()))

sumlist = []
mysum = 0
answer = []

for i in mylist:
    mysum += i
    sumlist.append(mysum)

for _ in range(M):
    i, j = map(int, input().split())

    if i == 1:
        answer.append(sumlist[j-1])
        continue

    answer.append(sumlist[j-1] - sumlist[i-2])

for i in answer:
    print(i)
