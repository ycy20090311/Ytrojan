# Ytrojan

`Ytrojan` is a troj generator based on the C/S structure in the TCP protocal, where the controller is treated as the **server** and the controlled terminal is treated as the **client**.

## How to use Ytrojan

Use a Python intepreter (`>=3.10`) to run `Main-Cmd.py`.

Result:
```
 __   ___             _             
 \ \ / / |_ _ __ ___ (_) __ _ _ __  
  \ V /| __| '__/ _ \| |/ _` | '_ \ 
   | | | |_| | | (_) | | (_| | | | |
   |_|  \__|_|  \___// |\__,_|_| |_|
                   |__/                         
                                      
Ytrojan $>
```  

## Use the command `generate` to generate the controlled script

```
Function Prototype: ControlAPI.Generate(BotSrc,BotIp,BotPort)
Command:            generate [PATH] [IP] [PORT]
1. [PATH] is the path to the controlled script
  e.g. : D:\bot.py  /home/bot.py
2. [IP] is the IP address of the controller
3. [PORT] is the port number of the controller
```

### Use the command `listen` to open the controller's port and wait for the connection from the controlled terminal of the reversed troj

```
Function Prototype: ControlAPI.Listen(ControlPort)
Command:            listen [port]

1. [ip] is the controller.
```  

<!-- MISTAKES HERE? --->
