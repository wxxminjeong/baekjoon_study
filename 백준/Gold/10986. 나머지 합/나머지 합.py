import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

prefix_sum = [0] * N
prefix_mod = [0] * N
prefix_sum[0] = num_list[0]
prefix_mod[0] = num_list[0] % M
count_mod0 = 0
combi = [0] * M
answer = 0

for i in range(0,N):
    if i == 0:
        prefix_sum[i] = num_list[i]
    else:
            prefix_sum[i] = num_list[i] + prefix_sum[i-1]
    prefix_mod[i] = prefix_sum[i] % M
    combi[prefix_mod[i]] += 1

for i in range(0, N):
    if prefix_mod[i] == 0:
        count_mod0 += 1

answer += count_mod0

for i in range(M):
    if combi[i] > 1:
        answer += (combi[i] * (combi[i]-1)) // 2

print(answer)

"""
(i,j) i부터 j까지 합이 M으로 나눠 떨어지면 정답 += 1

A[0] ~ A[8]까지의 합이 M으로 나눴을 때 나머지가 2인데
A[0] ~ A[2]까지의 합이 M으로 나눴을 때 나머지가 2이면
A[3] ~ A[8]까지의 합을 M으로 나누면 나누어 떨어짐

prefix_mod 가 같은 i-1과 j의 조합 개수를 세면 됨
"""