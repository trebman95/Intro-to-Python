# The following program takes a user's name and greets them back.
# Modify the code to use a function to print the greeting instead.

#user_name = input("What's your name: ")
#greet = f"Hello {user_name}!"
#print(greet)

#def greet():
#    user_name = input('What is your name: ')
#    print(f'Hello {user_name}!')
#greet()

def greet(name):
    print(f'Hello {name}!')

user_name = input('What is your name: ')
greet(user_name)


