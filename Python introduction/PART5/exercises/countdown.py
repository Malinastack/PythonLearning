def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)
    else:
        print(n)
        print('stop')


countdown(5)