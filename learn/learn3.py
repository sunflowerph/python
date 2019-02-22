#coding=utf-8
#python 100例

# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def question1():#原答案
    l1 = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if k != i and k != j and i!=j:
                    num=i*100+j*10+k
                    l1.append(num)
    print '数字的个数为： ' + str(len(l1))
    print '分别是：' + str(l1)


def question1_1():
    l = []
    for i in range(1, 5):
        num1 = i * 100
        for j in range(1, 5):
            if i != j:
                num2 = num1 + j * 10
                for k in range(1, 5):
                    if k != i and k != j:
                        num = num2 + k
                        l.append(num)
    print '数字的个数为： '+str(len(l))
    print '分别是：'+str(l)

# question1()
# question1_1()

#题目2：题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到10
# 0万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#题目3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#题目4：输入某年某月某日，判断这一天是这一年的第几天？
def question4():
    y = int(raw_input('请输入年份：'))
    m = int(raw_input('请输入月份：'))
    d = int(raw_input('请输入具体为某日：'))
    months=[0,0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if 1<=m<=2:
        totledays=months[m]+d
    elif 2<m<=12:
        if (y % 100 == 0 and y % 400 == 0) or y % 4 == 0:
            totledays=months[m]+d+1
        else:
            totledays=months[m]+d
    else:
        print '月份输入有误'

    print '现在是这一年的第'+str(totledays)+'天'

# question4()

#题目5：输入三个整数x,y,z，请把这三个数由小到大输出。
def question5():
    x=int(raw_input('请输入x:'))
    y=int(raw_input('请输入y:'))
    z=int(raw_input('请输入z:'))
    l1=[x,y,z]
    l1.sort()
    print l1

def question5_1(): #原答案
    l = []
    for i in range(3):
        x = int(raw_input('integer:\n'))
        l.append(x)
    l.sort()
    print l

# question5()
# question5_1()

#题目6：斐波那契数列。
#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
def question6(n):
    if n==1:
        l=[0]
    if n==2:
        l=[0,1]
    if n>2:
        x=0
        y=1
        l = [x, y]
        for i in range(n-2):
            l.append(x+y)
            x,y=y,x+y

    print l
#question6(3)
