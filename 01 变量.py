'''
1、什么是变量
    量：记录现实世界中的某种状态
    变：记录的状态是需要经常变化的
2、为什么要有变量
    一种机制能够反映或者说是保存下来程序执行时状态以及状态的变化
3、如何用变量

'''

#1、如何定义变量，变量定义为三部分
#变量名：专门用来访问到变量值的
#=赋值符号：将值与变量名绑定到一起
#值：是我们存储的数据（存到内存），用来表示现实世界中的某种状态
# level=0
# age=18
# name='anakin'
# age=19
# print(age)

#2、变量名的定义规范
'''
#1. 变量名只能是 字母、数字或下划线的任意组合
#2. 变量名的第一个字符不能是数字
#3. 关键字不能声明为变量名['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#3、变量名的命名风格

'''
#驼峰体:在Python中变量名的命名不推荐使用驼峰体
AgeOfOldboy = 56 
NumberOfStudents = 80
#下划线(推荐使用)
age_of_oldboy = 56 
number_of_students = 80
'''

#4、定义一个变量包含三个特征：
#id:变量值的身份证号，用来反映变量值在内存中的位置
#type：变量值的类型
#value：变量值

# age=18
#
# print(id(age))
# print(type(age))
# print(age)

# is ： 判断变量值的ID号是否相等
# ==  : 判断变量的值是否相等
#id不相同，值可以相同
#id相同，值一定相同


#5、变量的内存管理器
#Python解释器自带垃圾回收机制
#会在变量值没有任何应用的情况下自动回收


#6、常量：不变的量
#在Python中没有定义常量的语法，约定俗成全大写变量名定义为常量

x=1000
y=1000

print(x == y)













































































