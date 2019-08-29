#-*- coding: utf-8 -*-

#import Speech.Recognition.HMM
#Speech.Recognition.HMM.train()

#from Speech.Recognition.HMM import train
#train()

#from Speech.Recognition.HMM import *
#train()

from string import *

def add(a, b):
    return a + b

def f():
    print "Python is becoming popular."
    if __name__ == "__main__":
        print add(1, 10)

f()

#class S1:
#    "Class S1"
#    a = 1

#print S1.a
#print

#S1.b = 2   # 클래스 이름 공간에 새로운 이름의 생성
#print S1.b
#print

#print dir(S1)
#del S1.b    # 이름 공간 S1에서 b삭제
#print dir(S1)
print

#class S1:
#    a = 1

#x = S1()  # x는 S1의 클래스 인스턴스
#print x.a

#x.a = 10  # 클래스 인스턴스 x의 이름 공간에 새로운 이름의 생성
#print x.a

#print S1.a  # 클래스 이름 공간과 클래스 인스턴스의
#print x.a

class S1:
    a = 1

x = S1()
print x.a

x.a = 10
print x.a

print S1.a

print

y = S1()
y.a = 300

print y.a
print x.a
print S1.a

print
print

class Simple:
    a = 200
    pass

s1 = Simple()
s2 = Simple()

s1.stack = [] # 동적으로 클래스 인스턴스 이름 공간 안에 새로운 변수(이름) stack 생성
s1.stack.append(1) # 값 추가
s1.stack.append(2)
s1.stack.append(3)

print s1.stack
print s1.stack.pop()
print s1.stack.pop()

print
print s1.stack # 최종 s1.stack값
#print s2.stack # s2에는 stack을 정의한 적이 없다.

print

class MyClass:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value

class Simple:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value



print
c = MyClass()   # 인스턴스 생성
c.set('egg')    # 메소드 set 호출
s = Simple()

print c.get()   # 메소드 get 호출
print c.value   # 인스턴스 변수에 직접 접근

print
c2 = MyClass()  # 인스턴스 생성
MyClass.set(c2, 'egg')
print MyClass.get(c2)
print c2.value


Simple.set(s, 'egg')

print

def set(i):
    print "set function outside function", i

class MyClass1:
    def set(self, v):
        self.value = v
    def incr(self):
        #self.set(self.value + 1)
        set(self.value + 1)
    def get(self):
        return self.value

c = MyClass1()
c.set(1)
print c.get()

print

c.incr()
print c.get()

print

class D:
    @staticmethod
    def spam(x, y):
        print 'static method', x, y

D.spam(1, 2)

print
d = D()
d.spam(1, 2)


class C:
    @classmethod
    def spam(cls, y):
        print cls, '->', y

class D(C):
    pass

d = D()
d.spam(3)

print C

print
C.spam(5)

print
c = C()
c.spam(5)

class Var:
    c_mem = 100   # 클래스 맴버 정의
    def f(self):
        self.i_mem = 200   # 인스턴스 정의
    def g(self):
        print self.i_mem
        print self.c_mem

print Var.c_mem

v1 = Var()
print v1.c_mem
# print v1.i_mem   # error
v1.f()
print v1.i_mem

print
v2 = Var()
v2.f()
print v2.i_mem

print
print "-" * 20

print v1.c_mem
print v2.c_mem

print
v1.c_mem = 50
print v1.c_mem
print v2.c_mem

print Var.c_mem


# __init__ : 생성자 메소드 (self 인자가 정의되어야 한다)
#            객체가 생성될 때 자동으로 불리어지는 메소드
# __del__  : 소멸자 메소드 (self 인자가 정의되어야 한다)
#            객체가 소멸 (메모리에서 해제)될 때 자동으로 불리어지는 메소드

from time import ctime, sleep

class Life:
    def __init__(self):                 # 생성자
        self.birth = ctime()            # 현재시간에 대한 문자열
        print 'Birthday', self.birth    # 현재 시간 출력
    def __del__(self):                  # 소멸자
        print 'Deathday', ctime()       # 소멸 시간 출력

def test():
    mylife = Life()
    print 'Sleeping for 3 sec'
#    sleep(3)        # 3초간 sleep(block) 상태에 있음 (CPU 점유 못함)

test()

class Integer:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return str(self.i)

i = Integer(10)
print i
print str(i)


print "*" * 50

class MyInteger1:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return str(self.i)
    def increment(self, x):
        self.i = self.i + x
        return self
    def sub(self, x):
        self.i = self.i - x
        return self

k = MyInteger1(10)
print k                  # 10
k = k.increment(5)
print k                  # 15
k = k.sub(10)
print k                  # 5


class Integer:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return str(self.i)
    def __add__(self, other):
        return self.i + other

i = Integer(10)
print i
print str(i)

print
i = i + 10
print i

print
i += 10
print i

class MyString:
    def __init__(self,  str):
        self.str = str
    def __div__(self, sep):   # 나누기 연산자 /가 사용
        return self.str.split(sep)
    __rdiv__ = __div__     # print "_" / m
    #__invert__ = __neg__

m = MyString("abcd_abcd_abcd")
print m / "_"  # sep
print m / "_a" # sep

print "_" / m
print "_a" / m

print
print m.__div__("_")

class MyCmp:
    def __cmp__(self, y):
        return 1 - y

c = MyCmp()
print c > 1    # c.__cmp__(1)을 호출, 반환값이 양수이어야 True
print c < 1    # c.__cmp__(1)을 호출, 반환값이 음수이어야 True
print c == 1   # c.__cmp__(1)을 호출, 반환값이 0이어야  True


class MyCmp2:
    def __lt__(self, y):
        return 1 < y

m = MyCmp2()
print m < 10   # m.__lt__(10)을 호출
print m < 2
print m < 1

print "*" * 50

class MyCmp3:
    def __eq__(self, y):
        return 1 == y

m = MyCmp3()
print m == 10
m1 = MyCmp3()
print m == 1

class MyCmp4:
    def __init__(self, value):
        self.value = value
    def __cmp__(self, other):
        if self.value == other:
            return 0
m2 = MyCmp4(10)
print m2 == 10

print "*" * 50
class Square:
    def __init__(self, end):
        self.end = end
    def __len__(self):
        return self.end
    def __getitem__(self, k):
        if k < 0 or self.end <= k:
            raise IndexError, k
        return k * k

s1 = Square(10)
print len(s1)
print s1[1]
print s1[4]
#print s1[20]

s1 = Square(10)
for x in s1:    # s1[0], s1[1], s1[2], s1[3] ... s1[9],
    print x,
print
print  "*" * 50
print list(s1)
print tuple(s1)

print "*" * 50

class MyDict:
    def __init__(self, d = None):
        if d == None: d = {}
        self.d = d
    def __getitem__(self, k): #key
        return self.d[k]
    def __setitem__(self, k, v):
        self.d[k] = v
    def __len__(self):
        return len(self.d)
    def keys(self):
        return self.d.keys()
    def values(self):
        return self.d.values()
    def items(self):
        return self.d.items()

m = MyDict()            # __init__ 호출
m['day'] = 'light'
m['night'] = 'darkness'
print m
print m['day']          # light
print m['night']        # darkness
print len(m)            # 2

m = MyDict({'one':1, 'two':2, 'three':3})
print m.keys()
print m.values()
print m.items()
