n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
total = 0

for i in range(n):
    total += scores[i]/max_score*100

avg = total / n

print(avg)