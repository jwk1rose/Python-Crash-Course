while True:

    try:
        num1 = input('Please input number1:')
        num2 = input('Please input number2:')
        output = int(num1) + int(num2)
    except ValueError:
        print("please input number")
    else:
        print(output)
