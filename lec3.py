'''
lec3
list and set
'''

my_list=[1,2,3,4,5]
print(type(my_list))

my_nested_list=[1,2,3,my_list]
print(my_nested_list)

my_list[0]=6
print(my_list)

print(my_list[1])

print(my_list[-1])

print(my_list[:3])

print(my_list[1:])

print(my_list[:])

x,y,z=['a','b','c']

print(x)
print(y)
print(z)

my_list.append(7) #adds a 7 to the end of list
print(my_list)

my_list.remove(5) #removes a 5 from the list
print(my_list)

my_list.sort() #puts list in ascending order
print(my_list)

my_list.reverse() #puts list in descending order
print(my_list)

print(my_list+[8,9]) #adds numbers to list I extends the list = +
my_list.extend([8,9])
print(my_list)

print(2 in my_list) #tells if it is true or falsly in list (make sure not a string)

print(9 in my_list)

print(5 in my_list)

print('hello\tworld')

print('hello\nworld')

print(len('hello world.'))

my_letters=['a','a','b','b','c']
print(my_letters)

print(set(my_letters))
my_letters_set=set(my_letters)
print('a' in my_letters_set)
print('b' in my_letters_set)
print('e' in my_letters_set)

print(list(my_letters_set)[0])