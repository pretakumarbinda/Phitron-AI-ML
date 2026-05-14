# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/V

string = input()
new_string = string.split("EGYPT")
for i in range(len(new_string)):
    if(len(new_string)-1 == i):
        print(new_string[i], end="")
    else:
        print(new_string[i], end=" ")