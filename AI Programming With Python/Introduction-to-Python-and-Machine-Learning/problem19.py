# https://www.hackerrank.com/challenges/no-idea/problem

# first line: n m
n, m = map(int, input().split())

# main array
arr = input().split()

# sets
A = set(input().split())
B = set(input().split())

happy = 0

for item in arr:
    if item in A:
        happy += 1
    elif item in B:
        happy -= 1

print(happy)