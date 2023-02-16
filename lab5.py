'''
lab 5
If Statements in Python
'''

#3.1

alien_color='red'

if alien_color=='red':
    print('you get 5 points')
    
#3.2    
alien_color='green'

if alien_color=='red':
    print('you get 5 points')
else:
    print('you got 10 points')
    
    
#3.3
favorite_fruits='apple','banana','cantalope'

if 'apple' in favorite_fruits:
    print('I love apples')
if 'banana' in favorite_fruits:
    print('I love bananas')
if 'cantalope' in favorite_fruits:
    print('I love cantalope')

#3.4
age=20
if age < 10:
    print('kid')
elif age< 10 or age < 20:
    print('teenager')
else:
     print('adult')
     if age > 65:
        print('elder')

