# Write a Python generator function called batch_generator. It should take a list of numbers (representing data samples) and a batch_size. The generator should yield one batch at a time as a list.

data = list(map(int,input().split()))
batch_size = int(input())

def generator(data,batch_size):
    for i in range(0,len(data), batch_size):
        yield data[i:i+batch_size]        

x = generator(data,batch_size)
print(next(x))
print(next(x))
print(next(x))