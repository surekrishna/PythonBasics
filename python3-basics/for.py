# Printing letter by letter in string
for letter in 'krish':
    print(letter)
print('-----------------------------------------------')
# Printing fruits array
fruits = ['apple','banana','orange']
for fruit in fruits:
    chars = 0
    for char in fruit:
        chars += 1
    print('Name of the Fruit %s and length is %s' % (fruit, chars))
print('-----------------------------------------------')
# Looping both with index and items
for index, fruit in enumerate(fruits):
    print('Index %s and item %s ' % (index, fruit))
print('-----------------------------------------------')
#Nested for Loop
for i in range(1,2):
    for j in range(1,11):
        print('%d x %d = %d' % (i, j, i*j))
    