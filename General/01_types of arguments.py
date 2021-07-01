'''
1.Positional arguments
Positional arguments are arguments that need to be included in the proper postion or order. The first positional
argument always needs to be listed first when the function is called.
The second and the third positional argument listed third, etc
'''


# def sub(a, b):
#     print(a-b)
# sub(100, 50)


# def sub(a, b):
#     print(a-b)
# sub(50, 100)    #### when we change position of argument output changes


'''
2.Keyword arguments
Keyword arguments (or named arguments) are values that, when passed into a function, are identifiable by specific
parameter names. A keyword argument is preceded by a parameter and the assignment operator,=

Keyword arguments can be linkened to dictionaries in that they map a value to a keyword.
'''

# def wish(name, msg):
#     print("Hello", name, msg)

# wish(name="Sarthak", msg="HBD")




# def wish(name, msg):
#     print("Hello", name, msg)

# wish(msg="HBD", name="Sarthak")



'''
3.Default arguments
Dafault arguments in python functions are those arguments that take default values....
if no explicit values are passed to these arguments from the funtion call
'''

# def wish(name="Datta"):
#     print("Hello", name, "Good Evening")

# wish("Sushant")




# def wish(name="Datta"):
#     print("Hello", name, "Good Evening")

# wish()   ## when we didn't pass anything it will consider default value



'''
4.arbitarary keyword arguments = **kwargs
If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the paramete name in the function definition.
'''





def sum(*n):
    result = 0
    for x in n:
        result= result+x
    print("The sum: ", result)
sum()

sum(10)
sum(10, 20)
sum(10,20,30)
sum(10,20,30,40)