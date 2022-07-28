y = int(input('Podaj liczbę: '))
x = y // 2

while x > 1:
    if y % x == 0:
        print(y, 'dzieli się przez', x)
        break
    x -= 1
else:
    print(y, 'jest liczbą pierwszą')



