'''
lab7 while loop in python
'''
#3.1
num = 0
while num <= 5:
    if num != 3:
        print(num)
    num += 1
#3.2
n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("5! =", fact)

#3.3
n = 1
total = 0
while n <= 5:
    total += n
    n += 1
print("Sum of first five positive integers:", total)

#3.4
n = 3
product = 1
while n <= 8:
    product *= n
    n += 1
print("Product of numbers from 3 to 8:", product)

#3.5
n = 8
r = 3
perm = 1
while r > 0:
    perm *= n
    n -= 1
    r -= 1
while r == 0:
    perm /= r+1
    r -= 1
print("Permutation of 8 objects taken 3 at a time:", perm)

#3.6
num_list = [12, 32, 43, 35]
while num_list:
    num_list.pop()
    print(num_list)
