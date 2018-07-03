dic={
    'egon1':{'password':'123','count':0},
    'egon2':{'password':'123','count':0},
    'egon3':{'password':'123','count':0},

}


while True:
    name=input('username>>: ')

    if not name in dic:
        print('用户不存在')
        continue
    if dic[name]['count'] > 2:
        print('尝试次数过多,锁定')
        continue

    password=input('password>>: ')


    if password == dic[name]['password']:
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
        dic[name]['count']+=1