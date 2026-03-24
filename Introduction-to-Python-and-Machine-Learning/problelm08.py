# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/H

n = int(input())

for i in range(n):
    number = input()
    if "101" in number or "010" in number:
        print("Good")
    else:
        print("Bad")
