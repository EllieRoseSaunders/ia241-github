'''
for loop
lecture 6
'''
    
#for num in [1,2,3]:
#    print(num) #this also causes everything([1,2,3]) to be printed down
   # print(num+1)
   # print(num+5)
   
    
#for c in 'this is lec6':#this makes all of the letters write the demo string vertically
#    print(c)
    
#for d in 'this is lec6.2'.split(): #adding .split() means it splits my words instead of letters
 #   print(d)
    
#for num in [1,2,3]:
#   if num>1:
#       print(num) #this if statement means code will only print those numbers which are greater than 1
       
'''range() function''''''generates arithmetic pogressions such as (1,5) as 0,1,2,3,4'''

for i in range(5):
    print(i)
    
for i in range(2,5):#starts at first part of range(n,m) starts on variable n and ends on number previous to what is variable m
    print(i)

for i in range(1+4):
    print(i)

for i in range(1,5,2):
    print(i)

''' Breakpoint --- right click on number for code line and select breakpoint --- symbolized withh red dot--- interpriter will pause at each breakpoint'''

'''Algorithm --- mechanical process for solving problems --- very challenging'''

num_list = [213,321,123,312,432]

possible_max_num= num_list[]

for num in num_list:
    if num > possible_max_num:
        possible_max_num = num
print(possible_max_num)