while True:
    try:
        print('Enter Number to print')
        user_input = int(input())
        if user_input < 0:
            raise ValueError('Please Enter positive number.')
        else:
            print('Entered input number is %d ' % user_input)
    except ValueError as e:
        print(e)