# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/p2-a2-ai-brightness-analyzer

pixels = input().split()
sum = 0
for i in range(len(pixels)):
    sum += float(pixels[i])
avg = sum/len(pixels)
if avg<85:
    print("Dark Image")
elif 85<=avg and avg<=170:
    print("Normal Image")
else:
    print("Bright Image")