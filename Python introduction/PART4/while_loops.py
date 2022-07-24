# while True:
#     n = int(input('Podaj liczbę'))
#     if n < 10:
#         print(n)
#         break
#     if n > 11:
#         print('Kontynuuuje')
#         continue # przechodzi do samej góry pętli
#     else:
#         print('N = 10')
y = int(input('Podaj liczbę: '))
x = y//2
print(x)
while x > 1:
    if y % x == 0:
        print(y, 'ma czynnik', x)
        break # konczy dzialanie petli
    x -= 1
else:
    print(y, 'jest liczbą pierwszą')




