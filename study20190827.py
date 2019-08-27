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