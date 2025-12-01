N = int(input())
score_list = list(map(int, input().split()))

max_score = score_list[0]
sum_score = 0

for score in score_list:
    if max_score < score:
        max_score = score

for score in score_list:
    sum_score += score / max_score * 100

print(sum_score / N)