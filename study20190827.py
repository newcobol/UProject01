print 'Hello Python !!!'

def f(x):
    return x * x

#X = [1, 2, 3, 4, 5]
#Y = []
#for x in X:
#    y = f(x)
#    Y.append(y)
#print Y

Y = map(lambda x: x * x + 4 * x + 5, range(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print Y

y = map(lambda x: len(x), ["Hello", "Python", "Programing"])
print y

y = []
for x in [1, 2, 3, 34]:
    if x > 2:
        y.append(x)
print y

print
print

print filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6])

print filter(lambda x: x > 2, [1, 2, 4, 3, 34])
print filter(lambda x: x > 2, (1, 2, 4, 3, 34))
print filter(lambda x: x < 'a', 'abcABCdefDEF')

print

print reduce(lambda x, y: x + y * y, range(1, 11), 0)

x = 0
for y in range(1, 11):
    x = x + y * y
print x

print reduce(lambda x, y: y + x, 'abcde')

t=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print reduce(lambda x, y : x + y, filter(lambda x: x % 2, t))

print reduce(lambda x, y : x + y, range(1, 11))
print filter(lambda x: x % 2, range(1, 11))

g = lambda x, y=10: x + y
print g(10)

print reduce(lambda x, y: x + y * y, range(1, 11), 0)

g = 10
h = 5

def f(a):
    h = a + 10
    b = h + a + g
    return b

print f(h)
print h
