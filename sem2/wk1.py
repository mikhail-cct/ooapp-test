# s = 'Global Variable'

# def check_for_locals():
#     local = 'this is local'
#     print(locals())

# check_for_locals()

# print(globals().keys())

# def hello(name='Jose'):
#     return 'Hello '+name

# print(hello())

# greet = hello

# print(greet)

# print(greet())

# del hello

# print(hello())

# print(greet())

# def hello(name='Jose'):
#     print('The hello() function has been executed')

#     def greet():
#         return '\t This is inside the greet() function'

#     def welcome():
#         return "\t This is inside the welcome() function"

#     print(greet())
#     print(welcome())
#     print("Now we are back inside the hello() function")

# hello()

# welcome()

# def hello(name='Jose'):

#     def greet():
#         print('\t This is inside the greet() function')

#     def welcome():
#         print("\t This is inside the welcome() function")

#     if name == 'Jose':
#         return greet
#     else:
#         return welcome

# x = hello(name = "Sam")

# x()

# print(hello()())

# def hello():
#     return 'Hi Jose!'

# def other(func):
#     print('Other code would go here')
#     print(func())

# other(hello)

# def new_decorator(func):

#     def wrap_func():
#         print("Code would be here, before executing the func")
#         func()
#         print("Code here will execute after the func()")
#     return wrap_func

# @new_decorator
# def func_needs_decorator():
#     print("This function is in need of a Decorator")

# func_needs_decorator()

# # Generator function for the cube of numbers (power of 3)
# def gencubes(n):
#     for num in range(n):
#         yield num**3

# for x in gencubes(10):
#     print(x)

# def genfibon(n):
#     """
#     Generate a fibonnaci sequence up to n
#     """
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b

# for num in genfibon(10):
#     print(num)

# def simple_gen():
#     for x in range(3):
#         yield x

# # Assign simple_gen 
# g = simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

s = 'hello'

#Iterate over string
for let in s:
    print(let)

s_iter = iter(s)

next(s_iter)

next(s_iter)