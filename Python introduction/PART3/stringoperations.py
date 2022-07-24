# escape characters

print('new line\nnew line')
print('\ttab')
print('\'hello\'')
print('"Hello"')
print('path\\to\\file')
print(r'path\to\file') # r - raw string
print('''Hello
This
is
triple\'\'\'''')

# basic operations

word = 'python'
print('Lenght of the string')
print(len(word))
print('concatenation of strings')
print('abc' + 'xyz')
print('Multiplication of strings')
print('Yes!' * 10)
print('Using for')
for c in word:
    print(c, end=' ')
print('if statement')
if 'pyt' in word:
    print('That\'s true!')

# string slicing
# [x:y:z] x - from, y - to (but without this element), z - step

print(word[0])
print(word[-1])
print(word[::2]) # you can omit any of parameters, by default z is +1
print(word[3:1:-1]) # returns ht because the step is -1 and x and y are mixed y is x and x is y

# doing same
print(word[1:3])
print(word[slice(1,3)])

print(word[::-1])
print(word[slice(None, None, -1)])

word2 = word[3:]
word3 = word2 + 'Hello'

print(word)
print(word2)
print(word3)

word2 = word2.replace('hon', 'hondziarze')
print(word2)

testing = 'xxxxPythonxxxxPythonxxxxPythonxxxxPythonxxxxPython'
testing2 = testing[:]
testing3 = testing[:]

print('Zastosowanie find w pętli')
while testing2.find('Python') != -1:
    where = testing2.find('Python')
    testing2 = testing2[:where] + 'Great' + testing2[(where+6):]

print(testing2)
print('zastosowanie replace')
# instead of using something like this ^^^ you can use replace
print(testing3.replace('Python', 'Great'))


where = testing.find('Python')
testing = testing[:where] + 'Java' + testing[(where + 6):]
print(testing)


# string format examples
x = 'Today is %d day of %s' % (17, 'July')
print(x)
y = 'Hello %(name)s your age is %(age)d'
values = {'name': 'Szymon', 'age': 23} # values = dict(name='Szymon, age=23)
print(y % values)
z = '{}, {}, {}'.format('Dog','Cat', 'Chicken')
print(z)
w = '{}, {} and {}'.format('Dog','Cat', 'Chicken')
print(w.split('and'))

somelist = list('jajko')
print(somelist)
parts = somelist[0], somelist[-1], somelist[1:3]


text4 = 'first=%s, second=%s, last=%s' % parts
print(text4)
text = 'pierwszy={0}, ostatni={1}, przedzial={2}'.format(*parts) # unpacking tuple to make individual arguments
# format akceptuje tylko ogólne argumenty funkcji zamiast wymagać krotki dla wielu lub pojedyńczej wartości
print(text)
print('Drugi')
# not working cause we can't use -1 or 1:3 in formatting pattern, look at first or second method
# text2 = 'pierwszy={0[0]}, ostatni={0[-1]}, przedzial = {0[1:3]}'.format(somelist)
# print(text2)
text3 = f'pierwszy={somelist[0]}, ostatni={somelist[-1]}, przedzial = {somelist[1:3]}'
print(text3)
cos = 'this is the first'
text5 = 'first=%s' % cos
print(text5)


def myformat(fmt, args):
    return fmt % args


print(myformat('%s, %s', (123,123)))
print(str.format('{}, {}', 88, 99))

# %[(nazwa)][opcje][szerokość][.precyzja]kod_typu
# opcje np - wyrównuje do lewej, + natomiast dodaje spacje lub '0' przed liczbami dodatnimi i znak - przed liczbami ujemnymi
x = '%+08.2f' % (1.23456789, )
print(x)
x = '%+010.2f' % (1.23456789, )
print(x)
x = '%+10.2f' % (1.23456789, )
print(x)

# wyciagnij 'aj' z tego lancucha znakow
S = 'j, aj, a'
w = S.split(',')
print(w[1])
z = S[2:5]
print(z)

# ile znakow "a\nb\x1f\000d"
print('a\nb\x1f\000d') # - 6

number = '512974617'
number2 = tuple(number)
print('{}{}{}-{}{}{}-{}{}{}'.format(*number))