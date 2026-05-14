#  Write a function power(base, exponent) that returns the result of base raised to exponent. If the exponent is not given, it should calculate the square.
in1 = list(map(int,input().split()))
if len(in1)==2:
    base = in1[0]
    exponent = in1[1]
else:
    base= in1[0]
    exponent = 2
    
def power(base, exponent):
    print(base**exponent)


power(base, exponent)