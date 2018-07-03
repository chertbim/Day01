#语法

# while 条件：
#     code1
#     code2
#     code3
#     ....


# user_of_db='anakin'
# pwd_of_db='13579'
#
# inp_user=input('pls input your name :')
# inp_pwd=input('pls input your pwd :')
#
# if inp_user == user_of_db and inp_pwd == pwd_of_db:
#     print('login successful')
# else:
#     print('error,pls try again')




# user_of_db='anakin'
# pwd_of_db='13579'
#
# while True:
#     inp_user=input('pls input your name :')
#     inp_pwd=input('pls input your pwd :')
#
#     if inp_user == user_of_db and inp_pwd == pwd_of_db:
#         print('login successful')
#     else:
#         print('error,pls try again')
#



# while+break 跳出本层循环


# user_of_db = 'anakin'
# pwd_of_db = '13579'
#
# while True:
#     inp_user = input('pls input your name :')
#     inp_pwd = input('pls input your pwd :')
#
#     if inp_user == user_of_db and inp_pwd == pwd_of_db:
#         print('login successful')
#         break
#     else:
#         print('error,pls try again')

# user_of_db = 'anakin'
# pwd_of_db = '13579'
#
# count=0
# while True:
#     if count == 3:
#         print('尝试次数过多')
#         break
#     inp_user = input('pls input your name :')
#     inp_pwd = input('pls input your pwd :')
#
#     if inp_user == user_of_db and inp_pwd == pwd_of_db:
#         print('login successful')
#         break
#     else:
#         print('error,pls try again')
#         count+=1

# user_of_db = 'anakin'
# pwd_of_db = '13579'
#
# count=0
# while count < 3:
#     # if count == 3:
#     #     print('尝试次数过多')
#     #     break
#     inp_user = input('pls input your name :')
#     inp_pwd = input('pls input your pwd :')
#
#     if inp_user == user_of_db and inp_pwd == pwd_of_db:
#         print('login successful')
#         break
#     else:
#         print('error,pls try again')
#         count+=1



# user_of_db = 'anakin'
# pwd_of_db = '13579'
#
# count=0
# while True:
#     if count == 3:
#         print('尝试次数过多')
#         break
#     inp_user = input('pls input your name :')
#     inp_pwd = input('pls input your pwd :')
#
#     if inp_user == user_of_db and inp_pwd == pwd_of_db:
#         print('login successful')
#         while True:
#             cmd=input('cmd>>>:')
#             if cmd == 'q' : break
#             print('命令[%s]运行' %cmd)
#         break
#     else:
#         print('error,pls try again')
#         count+=1


# user_of_db = 'anakin'
# pwd_of_db = '13579'
#
# tag=True
# count=0
# while tag:
#     if count == 3:
#         print('尝试次数过多')
#         break
#     inp_user = input('pls input your name :')
#     inp_pwd = input('pls input your pwd :')
#
#     if inp_user == user_of_db and inp_pwd == pwd_of_db:
#         print('login successful')
#         while tag:
#             cmd=input('cmd>>>:')
#             if cmd == 'q' :
#                 tag=False
#                 break
#             print('命令[%s]运行' %cmd)
#
#     else:
#         print('error,pls try again')
#         count+=1





#while+continue :跳过本次循环，进入下一个循环

# n=0
# while n < 8:
#     if n == 4:
#         n+=1
#         continue
#     print(n)
#     n+=1




#强调，continue一定不要加到代码最后一步






user_of_db = 'anakin'
pwd_of_db = '13579'

tag=True
count=0
while tag:
    if count == 3:
        print('尝试次数过多')
        break
    inp_user = input('pls input your name :')
    inp_pwd = input('pls input your pwd :')

    if inp_user == user_of_db and inp_pwd == pwd_of_db:
        print('login successful')
        while tag:
            cmd=input('cmd>>>:')
            if cmd == 'q' :
                tag=False
                break
            print('命令[%s]运行' %cmd)

    else:
        print('error,pls try again')
        count+=1
