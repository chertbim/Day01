# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 每个用户输错三次后退出程序
# 可以支持多个用户登录

user_info = {                                                       #用户信息，词典
    'anakin': {'pwd': '666', 'count':  0},                      #用户名+密码+锁定计数
    'luke': {'pwd': '999', 'count': 0},                         #用户名+密码+锁定计数
    'ObiWan': {'pwd': '123', 'count': 0},                       #用户名+密码+锁定计数
    'Yoda' : {'pwd': '000', 'count': 0},                        #用户名+密码+锁定计数
}
tag = True                                                        #变量名tag初始值为真
count_a = 0                                                        #变量名count_a初始值为0
while tag:                                                        #while循环开始判断 值为真
    name = input('请输入您的用户名 :')                           #输入用户名

    if count_a > 2:                                               #当计数大于2时
        print('尝试次数过多,程序终止服务')                      #输出内容：尝试次数过多
        break                                                     #终止循环

    if not name in user_info:                                    #如果输入的用户名不在用户信息表单中
        print('用户不存在')                                      #输出内容：用户不存在
        count_a += 1                                              #变量名count_a数值+1
        continue                                                 #跳出当前循环

    if user_info[name]['count'] == 3:                           #如果用户表单信息中的计数器数值等于3
        print('该账号因尝试次数过多而被锁定,程序终止服务')     #输出内容：账号被锁定
        tag = False                                              #变量名tag值修改为否
        continue                                                 #跳出当前循环

    password = input('请输入您的密码 :')                        #输入密码

    if password == user_info[name]['pwd']:                      #判定如果输入的密码与表单信息中对应用户的密码相符
        print('登陆成功，欢迎%s' %(name))                      #输出内容：登陆成功
        while tag:                                               #while循环开始判断 状态为真
            cmd = input('cmd>>>:')                              #定义变量CMD等于'cmd>>>:'+输入内容
            if cmd == 'q':                                      #如果CMD中输入内容为Q
                tag = False                                     #变量名tag值修改为否
                break                                           #终止循环
            print('命令[%s]运行' %cmd)                         #输出内容：运行输入的命令

    else:                                                       #如果上述if都不符合
        print('密码错误，请重新登陆')                          #输出内容：密码错误
        user_info[name]['count'] += 1                          #变量词典user_info中对应用户名的计数器值+1
