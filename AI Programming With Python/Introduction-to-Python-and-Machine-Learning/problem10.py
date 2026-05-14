# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/b1-smart-light-pilot-threshold

in1 = input()
numbers = in1.split()
brightness = float(numbers[0])
threshold = float(numbers[1])
if brightness>= threshold:
    print("ON")
else:
    print("OFF")