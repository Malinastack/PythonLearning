while True:
    try:
        number1 = int(input('Give me first number: '))
        number2 = int(input('Give me second number: '))
        answer = number1 + number2
        print(answer)
    except ValueError:
        print('Wrong number, please try again')