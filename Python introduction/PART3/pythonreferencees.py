
# there b is equal to COPY of a, so when we change b, nothing changes in a
a = [1,2,3]
b = a[:]
b[0] = 5

print(a)
print(b)

# there b is equal a, so when we are making some changes in b, a also changes
x = [1,2,3]
y = x
x[0] = 5

print(x)
print(y)