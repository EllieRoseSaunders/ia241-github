''''
lec4 Dictionary and Tuple
'''

#my_tuple = ('a','b','c','d','e')
#print(type(my_tuple))

#print(my_tuple[0:2])

'''a tuple has both ('x',) essencially both perenthesis and quotation marks'''

#my_2nd_tuple = ('a','b','c','d','e')
#print(my_2nd_tuple)

'''Dictionary - key value pairs - created with {} or dict() - values can be string, number, list, variable, or dictionary'''

my_car = {  
         'color':'red',
         'maker':'toyota',
         'year':2015
         }
         
#print(my_car['color'])
#print(my_car['maker'])
#print(my_car['year'])

print(my_car.items()) #-->dict_items([('color', 'red'), ('maker', 'toyota'), ('year', 2015)])

print(my_car.keys()) #-->dict_keys(['color', 'maker', 'year'])

print(my_car.values()) #-->dict_values(['red', 'toyota', 2015])

print(my_car.get('color'))
print(my_car['color'])


my_car['model']='venza'#inserted new word and definition into dictionary madel-venza
print(my_car)

my_car['year']=2020 #updating an existing value/term/definition
print(my_car)

print(len(my_car)) #len() function checks how many dictionary pairs there are

print('color'in my_car)#can only be used for checting word not definition used to determine if there is one present

print('color'in my_car.values())#is color a value - no
