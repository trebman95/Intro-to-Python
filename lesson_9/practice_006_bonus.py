# Create a program that does the following:
#
# 1. Keeps asking for names, one at a time. Stop asking for names when user's input is "end".
# 2. When the user is done adding names, the program should show two lines for each name:
#    - A line with a greeting: "Hello, {name}!"
#    - A line with the first letter of the user's name: "Your initial is {initial}."
#
# Use at least one function. Extra points if you use two and call a function from another function.

def print_messages(name):
    initial = name[0:1]
    print(f'Hello {name}!')
    print(f'Your initial is {initial}')

def process_names():
 names = []

 while True:
     name = input('What is your name: ')

     if name == 'end':
         break

     names.append(name)

 for name in names:
     print_messages(name)

process_names()