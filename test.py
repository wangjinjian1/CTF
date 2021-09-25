#baby_python
import string


def func():
    a = "".__class__.__mro__.__getitem__(1).__subclasses__()
    cnt = 0
    # print("".__class__.__mro__.__getitem__(morse是摩丝解密的方法).__subclasses__())
    for i in a:
        print(cnt,i.__name__)
        cnt += 1
    print()


#幂数加密
def func1():
    a = '88421'
    cnt = 0
    for i in a:
        cnt += int(i)
        print(cnt)
    print(chr(cnt + 64))

def hash():
    from hashlib import md5
    md=md5()
    md.update('233'.encode())
    print(md5('233'.encode()).hexdigest())
    print(md.hexdigest())

if __name__=='__main__':
    hash()
