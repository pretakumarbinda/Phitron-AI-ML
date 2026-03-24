# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/p2-a3-ai-bias-detector


in1 = input().split()
a_count = 0
b_count = 0
for i in range(len(in1)):
    if in1[i]=="A":
        a_count+=1
    else:
        b_count+=1
        
total = a_count+b_count
if a_count/total>0.7:
    print("Biased Model")
elif b_count/total>0.7:
    print("Biased Model")
else:
    print("Fair Model")