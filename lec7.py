'''
lec7
while loop
continue, break, and pass
'''
'''
#i=5
#while i>0:
#    print(i) #written in this way will go on forever because there is no condition where code becomes false andd no longer infident
for item in ['a','b']:
    print(item)
    i=5
    while i>0: #break only works on the smallest for loop in the code (only works on the closess loop)
        i = i -1 #end at -1 --- writen before print it is 43210
        print(i)
        # i = i-1 #if written after print it is 54321
        if i == 3:
            break #breaks out the smallest enclosement of a for or with loop
    '''
'''
countinue statement
'''
'''
i = 5
while i >0:
    i=i -1
    print(i)
    if i ==3:
        continue
    print(i)
'''   
'''
i = 5
while i >0:
    i=i -1
    print(i)
    if i ==3:
        pass
    print(i)
    '''
'''#try -- except error code - shows code with an error as printing error    
try:
    print(21/0)
except:
    print('error')'''
    
i = 5
while i >0:
    try:
        print(1/(i-3))
    except:
        pass
        i=i -1