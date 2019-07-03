# try, except, finally
try:
    print('In try block')
    print(1/0)
except ValueError as e:
    print(e)
finally:
    print('In finally block')
print('--------------------------------------------')

