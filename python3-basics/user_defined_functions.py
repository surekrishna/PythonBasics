# Call a function that performs a task and has no return value
def print_the_message():
    print('Hello im just function, with no Return value')
print_the_message()
print('-------------------------------------------------')
# Adding two numbers 
def add_two_numbers(num1, num2):
    return num1 + num2
result = add_two_numbers(10,20)
print('sum of two numbers is %d : ' % result)
print('-------------------------------------------------')
# String multiplier
def string_multiplier(string_arg, number):
    return string_arg * number
print('String multiplier %s ' % string_multiplier('a',5))