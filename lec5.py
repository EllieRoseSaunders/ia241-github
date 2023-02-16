'''
lecture 5 
            if statement
'''
#import this

#print(     1+15+
           # 4563)   #WHITE SPACE EXAMPLE

#a =[1,2,3]
#b =[1,2,3]

#print(id(a))
#print(id(b))
#print(id([1,2,3]))

# == means compare the values of two objects

#print(a==b) #same values (1,2,3)
#print(a is b) # different id's [140353728095488,  140353726866928] own specific identifier


#c=1
#d=1 #same value do they have same id
#print(id(c))
#print(id(d))
#print(id(1)) #all have the same id - same values(integer) same id - if it is the same list they are considered seperate and do not have the same id

#NONE Type - datatype of its own that indicates no value
#in python only 'None' can be None

#a=None

#print(id(a))
#print(id(None))#both have same id

#print(a is None)
#print(a==None) #most of the time we use this value x.    true


#x=[]#empty list
#print(x is None)#does an empty list = None?    true'

#x=""
#print(x is None)# 'is' operator means x is x / x=x.    false'

#x={}
#print(x is None)  #ONLY NONE IS NONE.     false'

#print(True and False)#=false'
#print(True or False)#=true'

#print(not True)#=false'
#print(not False)#=true'

#print(not 0)#not will only be true or false - not 0 = true'

#print(not '0') # = false'

#print(not True) #false'

#print(1>2)    #false'''

if 2>1 :   
    print('2>1')         #will be executed if true but not if false'''
    print('another 2>1')    #will be executed if true but not if false'''
    if 3>1:
        print('3>1')
else:
    print('else statement')

print('out of if block')    

if 2>1:
    print('2>1')
    
elif 3>1:
    print('3>1')
    
else:
    print('else')