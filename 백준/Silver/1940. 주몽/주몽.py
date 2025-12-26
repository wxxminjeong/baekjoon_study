import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
list_materials = list(map(int, input().split()))
list_materials.sort()
count = 0
sum = 0
start_index = 0
end_index = len(list_materials) - 1

while start_index < end_index:
    sum = list_materials[start_index] + list_materials[end_index]
    if sum == M:
        count += 1
        end_index -= 1
    elif sum > M:
        end_index -= 1
    elif sum < M:
        start_index += 1

print(count)