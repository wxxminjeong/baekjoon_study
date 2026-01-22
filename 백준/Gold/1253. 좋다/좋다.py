import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
count = 0

for target_index in range(N):
    start_index = 0
    end_index = N-1

    while start_index < end_index:
        if start_index == target_index:
            start_index += 1
            continue
        if end_index == target_index:
            end_index -= 1
            continue
        
        temp_sum = num_list[start_index] + num_list[end_index]
        if temp_sum < num_list[target_index]:
            start_index += 1
        if temp_sum > num_list[target_index]:
            end_index -= 1
        if temp_sum == num_list[target_index]:
            count += 1
            break

print(count)