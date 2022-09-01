# Ytrojan

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
