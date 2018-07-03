#1、整形 int
#作用：记录年龄、等级、手机号、邮编号码等等
# age=38 #age=int(28)
# print(type(age))
# print(age+2)

#2、浮点型：
#作用：记录生个、体重、薪资

# salary=9.5  #salary=float(9.5)
# # print(type(salary))


#3、字符串
#定义：在单引号、双引号、三引号内包含一串字符
#作用：记录描述性质的状态，姓名、住址等等
#区别1、三引号可以存放多行数据
#区别2、注意配对



#字符串可以使用+和*


#4、列表类型（list）
#定义：在[]内用逗号隔开，存放多个任意类型的值
#作用：用于存放多个值，并且可以按照索引灵活取出任意位置对应的值

#students=['egon','alex','wupeiqi',] #students=list(['egon','alex','wupeiqi',])

# a=[1,4,5.5,[119,840],'aaaa',[999,['千寻琳',000]]]
# print(a,type(a))
# print(a[3][1],a[4])
# print(a[5][1][0])

#5、字典类型dict
#定义方式：在｛｝内用逗号隔开多个元素，每一个元素都是k:v的形式，其中v可以是任意数据类型，而k大部分都应该是字符串类型
#作用：用来寸多个值，但是每一个值都有一个明确的key来与其对应，key对value应该具有描述性的功能
#当存放的多个值有明显的种类区分时，建议用字典
#当存放的多个值有一样的种类区分时，建议用列表
# info=dict({'name':'egon','age':18,'sex':18})
# info={
#         'name':'egon',
#         'age':18,
#         'sex':'male',
#         'compay_info':['oldboy','BJ',18],
#      }

#print(info['age'])
#print(info['compay_info'][1])

info={
        'name':'egon',
        'age':18,
        'sex':'male',
        'compay_info':['oldboy','BJ',18],
     }


print(info['name'])

#6、布尔值
#定义：就两个：Ture，False
#作用：用于判断真假


















































































