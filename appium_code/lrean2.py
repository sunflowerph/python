'''
class A(object):
    def bash(self):
        print 'hello'

class B(A):
    def bash(self):
        print 'hi'

b=B()
'''

#b.bash()
class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print 'a=', self.__a, 'b=', self.__b
a1=A(10,20)
a1.myprint()


