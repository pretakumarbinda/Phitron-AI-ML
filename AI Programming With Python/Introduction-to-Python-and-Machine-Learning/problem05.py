# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E

in1 = int(input())
in2 = input()
numbers = in2.split()
index = -1
lowest_num = int(numbers[0])
for i in range(in1):
    if(int(numbers[i])<lowest_num):
        lowest_num = int(numbers[i])

for i in range(in1):
    if(int(numbers[i])==lowest_num):
        index = i
        break


print(lowest_num, end=" ")
print(index+1)
    