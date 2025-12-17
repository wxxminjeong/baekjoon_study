import sys
input = sys.stdin.readline

N, M = map(int, input().split())

my_list = [[0] * (N + 1)]
prefix_sum = [[0] * (N+1) for _ in range(N + 1)]

for i in range(N):
    temp_row = [0] + list(map(int, input().split()))
    # temp_row = [0] + [int(x) for x in input().split()]
    my_list.append(temp_row)

for row in range(1, N+1):
    for col in range(1, N+1):
        prefix_sum[row][col] = (prefix_sum[row-1][col] + prefix_sum[row][col-1]
                                - prefix_sum[row-1][col-1] + my_list[row][col])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])