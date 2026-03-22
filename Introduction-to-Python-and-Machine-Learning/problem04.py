test_case = int(input())
for i in range(test_case):
    in1 = int(input())
    if in1 ==0:
        print(0)
        continue
    
    while(in1>0):
        print(in1%10, end=" ")
        in1 = in1 // 10
    print()
