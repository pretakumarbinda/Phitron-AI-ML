in1 = int(input())
in2 = input()
numbers = in2.split()
E=0;O=0;P=0;N=0;

for i in range(in1):
    if(int(numbers[i])%2==0):
        E+=1;
    else:
        O+=1;
    
    if(int(numbers[i])>0):
        P+=1;
    elif(int(numbers[i])<0):
        N+=1;
    

print("Even: ",E)
print("Odd: ",O)
print("Positive: ",P)
print("Negative: ",N)