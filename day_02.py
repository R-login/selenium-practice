from datetime import datetime
def login(name,passwd):
    """
    传账号和密码,如果账号和密码不对,返回相应提示信息和操作时间
    :param name: 账号 类型 :str 示例：‘admin111’
    :param passwd: 密码 类型 :int 示例：123456
    :return: 提示信息和操作时间 类型 str 示例:("登录成功","2022-10-21 16:00:00")
    """
    msg = '登录成功'
    msg2 = '登录失败'
    login_time = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    if name == 'admin' and passwd == 123456:
        return msg,login_time
    else:
        return msg2,login_time

def over(number):
    for i in range(number):
        if i == 2:
            return '执行结束'
        else:
            print(i)

def prRint(m):
    for i in range(m):
        print('*',end=' ')
    print()

def hang(n,m,/):
    for _ in range(n):
        prRint(m)

def sds(*v,arg=2):

    print(v)
    return arg

def sfs(**kwargs):
    print(kwargs.get('n'))
    print(*kwargs)

def last_day(**kwargs):
    print(kwargs)

last_day(a=1)






















