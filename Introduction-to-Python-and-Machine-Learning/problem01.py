inp = input()

numbers = inp.split()

x = int(numbers[0])
y = int(numbers[1])

LastDigit_x = x%10
LastDigit_y = y%10
print(LastDigit_x+LastDigit_y)