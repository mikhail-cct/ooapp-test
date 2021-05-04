# x = 25

# def printer():
#     x = 50
#     return x

# print(x)
# print(printer())

# name = 'This is a global name'

# def greet():
#     # Enclosing function
#     name = 'Sammy'
#     def hello():
#         print('Hello '+name)   
#     hello()

# greet()
# print(name)

# x = 50

# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)

# func(x)
# print('x is still', x)

# x = 50

# def func():
#     global x
#     print('This function is now using the global x!')
#     print('Because of global x is: ', x)
#     x = 2
#     print('Ran func(), changed global x to', x)

# print('Before calling func(), x is: ', x)
# func()
# print('Value of x (outside of func()) is: ', x)

# def myfunc(*args):
#     print(sum(args)*.05)

# myfunc(40,60,20)

# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
#     else:
#         print("I don't like fruit")

# myfunc(fruit='pineapple')

# myfunc()

# def myfunc(*args, **kwargs):
#     if 'fruit' and 'juice' in kwargs:
#         print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
#         print(f"May I have some {kwargs['juice']} juice?")
#     else:
#         pass

# myfunc('eggs','spam',fruit='cherries',juice='orange')

# def vol(rad):
#     return (4/3)*(3.14)*(rad**3)
# # Check
# print(vol(2))

def ran_check(num,low,high):
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')