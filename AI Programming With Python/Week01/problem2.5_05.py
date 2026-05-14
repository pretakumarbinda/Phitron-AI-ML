# Given a list [1,2,3,4,5,6], use filter() to select even numbers and map() with lambda to square them.

list1 = [1,2,3,4,5,6]
out = list(map(lambda x: x**2, (filter(lambda x: x%2==0,list1))))

print(out)

# print(list(filter(lambda x: x%2==0,list1)))