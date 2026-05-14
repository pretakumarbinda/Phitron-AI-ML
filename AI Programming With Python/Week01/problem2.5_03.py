#  Given a list [1,2,3,4], use map() and lambda to create a new list with squares of each number.

list1 = [1,2,3,4]

new_list = list(map(lambda x:x**2,list1))
print(new_list)