n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
for idx, score in enumerate(scores):
    scores[idx] = score / max_score * 100
print(sum(scores) / n)