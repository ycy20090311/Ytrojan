import socket

def Caesar(i,string1):#凯撒密码加密与解密
    string2 = ''
    if i == 0:#加密
        for a in string1:string2 = string2 + chr(ord(a)+319)
    elif i == 1:#解密
        for a in string1:string2 = string2 + chr(ord(a)-319)
    return string2


if '__main__' == __name__:
    t = socket.socket()
    t.bind(('', 12345))
    t.listen(1)
    c,ip = t.accept()
    while True:
        cmd = input('$>')
        if cmd == '':print('')
        else:
            c.send(Caesar(0,cmd).encode())
            print(Caesar(1,c.recv(2048).decode()))
    c.close()
    t.close()
