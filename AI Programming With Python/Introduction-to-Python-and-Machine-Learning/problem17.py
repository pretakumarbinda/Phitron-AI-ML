# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/p2-a4-ai-keyword-counter

sentence = input().split()
count = 0
if "ai" in sentence:
    count += 1
if "data" in sentence:
    count += 1
if "model" in sentence:
    count += 1
if "learn" in sentence:
    count += 1
if "train" in sentence:
    count += 1
if "neural" in sentence:
    count += 1
    
    
if count >= 2:
    print("AI Detected")
else:
    print("Not AI Related")