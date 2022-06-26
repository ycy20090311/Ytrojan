import socket

def Caesar(i,string1):#凯撒密码加密与解密
    string2 = ""
    if i == 0:#加密
        for a in string1:
            string2 = string2 + chr(ord(a)+4)
    elif i == 1:#解密
        for a in string1:
            string2 = string2 + chr(ord(a)-4)
    return string2

if "__main__" == __name__:
    t = socket.socket()
    t.connect((sys.argv[1],int(sys.argv[2])))
    while True:
        cmd = input("$>")
        if cmd == "":print("")
        else:
            t.send(Caesar(0,cmd).encode())
            print(Caesar(1,t.recv(2048).decode()))
    t.close()
