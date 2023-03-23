'''
lec9 python functions
'''

def addition(a,b):
    result = a+b 
    return result
#    this is an example of a function - its name is My_function a and b are the variables 
    #you imput ot change every time print the function
    # result declares what you want the function to do
    #return demands the results of a+b or the variables

#print(addition(1,2))

#print(addition(128,32))

def multiplication(c,d):
    result = c*d
    return result
    
#print(multiplication(5,33))

'''
arguments and parameters
a = piece of info thats fassed from a function call to a function
p = insted function arguments are assigned to variables parameters -
- basically variables a, b, c, and d in above example
'''

def example_x (g,h = 0):
    
    result = g+h
    print( 'g is', g)
    print( 'h is', h)
    
    return result
    
#print(example_x(1))
#print(example_x(h=2, g=3))

#print(example_x(h=123, g=27))

def absolute_value (z):
    if type(z) is str:
        return('wrong data type')
    elif z > 0:
        return z
    else:
        return -z
#print(absolute_value(9))

#print(absolute_value(-19))

#print(absolute_value(-43))

#def sigma (n,m):
#    result = n+(n+1)+(m-1)+m
 #   return result
#print(sigma(5,1))
#print(sigma(1,6))

#def pi (r,s):
#    result = r*(r+1)*(s-1)*s
 #   return result
#print(pi(3,5))
#print(pi(1,6))



def sigma_2 (n,m):
    result = 0
    for i in range(n,m+1):
        result = result + i
        return(result)

#print(sigma_2(5,1))


def pi_2 (r,s):
    result = 1
    for i in range(r,s+1):
        result = result *i
    return (result)

print(pi_2(5,1))

def cal_f(e):
    if e == 0:
        return 1
    else:
        return e * cal_f(e-1)
    print(cal_f(1))
    
def cal_p(l,v):
    return cal_p(l)/cal_p(l-v):
print(cal_p)