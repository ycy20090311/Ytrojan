## 语言

[English](README_EN.md) | [中文](README.md)

## 什么是Ytrojan

Ytrojan是用Python编写的开源远控木马     

1. 控制多台Bot  
2. 远程加载恶意代码    
3. 执行Shell   
4. 上传与下载文件
5. 远程执行Python脚本   
6. 屏幕截图  
7. 获取可用摄像头列表  
8. 调用摄像头拍照  

## Ytrojan的依赖库     

Ytrojan需要`opencv-python`和`Pillow`库  
您可以直接`pip install -r requirements.txt`  

## 怎么使用Ytrojan

### 使用Python3.10或更高版本解释器运行`src/main_cli.py`  
    __   ___             _             ____  
    \ \ / / |_ _ __ ___ (_) __ _ _ __ |___ \ 
     \ V /| __| '__/ _ \| |/ _` | '_ \  __) |
      | | | |_| | | (_) | | (_| | | | |/ __/ 
      |_|  \__|_|  \___// |\__,_|_| |_|_____|
                      |__/   
 
### 命令介绍  

#### 1. generate命令   

格式: `generate <host> <port> <path>`  
API: `control.generate(host:str,port:str,path:str) -> None`   
该命令用来生成bot端的恶意Python脚本,`host`,`port`均为control端地址,`path`为保存生成路径   

#### 2. service命令     

格式: `service <host> <port>`      
API: `control.serice(socket:socket.socket) -> None`   
该命令用来启动处理bot连接的子线程,`host`,`port`均为control端地址  

#### 3. listbot命令  

格式:`botlist`  
该命令用来输出目前连接至control的bot,输出bot编号和网络地址  

#### 4. sysinfo命令  

格式: `sysinfo <id>`   
API: `control.sysinfo(socket:socket.socket) -> dict`    
该命令用来输出bot的详细信息 包括操作系统,网络名称,硬件信息等  

#### 5. shell命令  

格式: `shell <id> <command>`   
API: `control.shell(socket:socket.socket,input:list[str],timeout:bool) -> tuple`    
该命令用来在bot上执行一条shell命令     

注意这里`control.shell`中`timeout`参数决定是否开启超时处理   
在使用`shell`命令时会开启   

#### 6. shell_nt命令   
 
格式:`shell_nt <id> <command>`   
API: `control.shell(socket:socket.socket,input:list[str],timeout:bool) -> tuple:`  
该命令同上 但不会开启超时处理   

#### 7. script命令    

格式:`script <id> <path>`   
API:`control.script(socket:socket.socket,local_path:str) -> tuple`   
该命令用来在bot端远程执行Python脚本   

#### 8. download命令 

格式:`download <id> <remote_path> <local_path>`   
API:`control.download(socket:socket.socket,remote_path:str,local_path:str) -> bool`   
该命令下载文件到本地,注意`remote_path`,`local_path`要指向一个文件,而不是目录

#### 9. upload命令 

格式:`upload <id> <local_path> <remote_path>`   
API:`control.upload(socket:socket.socket,local_path:str,remote_path:str) -> bool`     
该命令上传文件到bot,注意`remote_path`,`local_path`要指向一个文件,而不是目录

#### 10. screenshot命令

格式:`screenshot <id> <path>`   
API:`screenshot(socket:socket.socket,local_path:str) -> bool`   
该命令用来在bot截屏,保存至本地,`local_path`要指向一个文件,而不是目录

#### 11. webcamlist命令  

格式:`webcamlist <id>`   
API:`control.webcamlist(socket:socket.socket) -> tuple`   
该命令获取bot可用摄像头列表和长宽信息  

#### 12. webcamsnap命令  

格式:`webcamsnap <id> <index> <path>`   
API:`webcamsnap(socket:socket.socket,id:int,local_path:str) -> bool`   
该命令调用bot对应编号的摄像头拍照并保存到本地,`local_path`要指向一个文件,而不是目录

#### 13. kill命令  

格式:`kill <id>`   
API:`control.kill(id:int) -> None`  
该命令用来关闭bot连接   

#### 14. exit命令   

格式:`exit`   
退出命令
  

## 写在最后  

如你所见,Ytrojan目前功能十分弱小   
我们还没有免杀模块,提权,跳板渗透内网...   
Ytrojan目前更像是一个中二初中生编写的小玩意   

Ytrojan日后可能会停更很长一段时间,由于我已经初三,且成绩并不好.  
在这期间,如果您有好的想法,可以提交Pr,我会很感谢您的 !
