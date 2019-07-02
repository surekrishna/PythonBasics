# if, elif, else conditions
number = 1
if number == 1:
    print('Number is %d' % number)
print('-----------------------------------------------')
if number == 2:
    print('Number is %d' % number)
elif number == 1:
    print('Number is %d' % number)
print('-----------------------------------------------')
if number == 10:
    print('Number is %d' % number)
elif number == 20:
    print('Number is %d' % number)
else:
    print('Number is Not 10 or 11, Number is %d' % number)
print('-----------------------------------------------')
# Nested if conditions
num = 30
if num > 10:
    if num < 40:
        print('Number is between 10 and 40')