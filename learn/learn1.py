#coding=utf-8
# a0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print (a0)
#
# a3 = [a0[s] for s in a0]
# print (a3)
#
#
# a=[[i,i*i ]for i in range(3)]
# print (a)
# a=[(1,2),(3,4)]
# print (dict(a))
# print (tuple(a))
# c=zip((1,2,3),(4,5,6))
# print (dict(c))
# def f(*args):
#     print (args)
# def n(**kwargs):
#     print (kwargs)
#
# a=f(1,2,3)
# b=n({'a':3})
# class A(object):
#     def go(self):
#         print ("go A go!")
#     def stop(self):
#         print ("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")
#
# class B(A):
#     def go(self):
#         super().go()
#         print ('go b go')
#
#
#
# b=B()
# b.go()

# def calc_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax += n
#         return ax
#     return sum
#
#
#
# print (calc_sum(1,2,3)())

from functools import reduce
# def f(x):
#     s=1
#     for i in range(1,x+1):
#         s=s*i
#     print (s)




# f(2)
# # f(3)
# # f(4)
# #
# #
# # f(3,[1,2,3])
# # f(2,[1,2,3])
# # f(1,[1,2,3])
# l=map(f,[1,2,3])
# print (list(l))
# n=reduce(f,[1,2,3,4,5,6])

#print(sum(range(1,101)))

# a={'a':1,'b':2}
# b={'c':3,'d':4}
#
# a.update(b)
# print (a)
#
# print (b)
# del a['a']
# print (a)
# a=[1,2,3,4,5,2,3,5]
# print (set(a))
#
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print (b)

# def f(**kwargs):
#     for k,v in kwargs.items():
#         print (k,v)
# f(name='peng',sex='femail',age=25)
#
# def n(*args):
#      print (args)
#
# n(1,2,3,4)

# s = "ajldjlajfdljfddd"
# # sum=lambda a,b : a*b
# # print (sum(1,2))

# dict1={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# print (type(dict1))  # type 返回数据类型
# print (dir(dict1)) #dir 返回这个数据类型下所有的方法和变量

#coding=utf-8
# h=input('请输入身高（单位：m）：')
# w=input('请输入体重（单位kg）：')
# H=float(h)
# W=float(w)
# BIM=H/W**2
# print('您的BIM指数是：',BIM)
# if BIM<18.5:
#     print('您的体重过轻！')
# elif 18.5<=BIM<25:
#     print('您的体重正常，请保持！')
# elif 25<=BIM<28:
#     print('您的体重过重，有点微胖哦！')
# elif 28<=BIM<32:
#     print('您的体重超重了，名副其实的小胖子！')
# else :
#     print('emmm....大胖子，说的就是你！')

#print (sum(range(101)))

