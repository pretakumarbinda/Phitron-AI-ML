# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/b5-majority-vote-gate-simple-ensemble

n = int(input())
y_count = 0
n_count = 0
for i in range(n):
    vote = input()
    if(vote == "YES"):
        y_count+=1
    else:
        n_count += 1

if y_count>=n_count:
    print("ACCEPT")
else:
    print("REJECT")