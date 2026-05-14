inp = input()
numbers = inp.split()

x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])

mini = min(x,y,z)
maxi = max(x,y,z)

print(mini, maxi)