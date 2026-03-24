# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/b4-mini-loss-tracker-average-monitor

n = int(input())
target = float(input())
sum = 0
for i in range(n):
    sum += float(input())
avg = sum/n
if avg<=target:
    print("PASS")
else:
    print("RETRY")