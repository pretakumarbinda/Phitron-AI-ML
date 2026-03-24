# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K

n = int(input())
digits = input()
sum = 0
for ch in range(n):
    sum = sum + int(digits[ch])
    
print(sum)