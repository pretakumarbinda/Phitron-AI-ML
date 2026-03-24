# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M

in1 = int(input())
in2 = input()
numbers = in2.split()

# for calculating lowest number and index

lowest_index = -1
lowest_num = int(numbers[0])
for i in range(in1):
    if(int(numbers[i])<lowest_num):
        lowest_num = int(numbers[i])

for i in range(in1):
    if(int(numbers[i])==lowest_num):
        lowest_index = i
        break

# for calculating highest num and index
highest_index = -1
highest_num = int(numbers[0])
for i in range(in1):
    if(int(numbers[i])>highest_num):
        highest_num = int(numbers[i])

for i in range(in1):
    if(int(numbers[i])==highest_num):
        highest_index = i
        break
    
    
# swaping

numbers[highest_index] = lowest_num
numbers[lowest_index] = highest_num


for i in range(in1):
    print(numbers[i], end=" ")
