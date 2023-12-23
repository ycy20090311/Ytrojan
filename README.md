## What is Ytrojan

Ytrojan is an open-source remote control Trojan written in Python.

1. Control multiple bots.
2. Load malicious code remotely.
3. Execute shell commands.
4. Upload and download files.
5. Execute Python scripts remotely.
6. Take screenshots.
7. Obtain a list of available webcams.
8. Take photos using the webcam.

## Dependencies of Ytrojan

Ytrojan requires the `opencv-python` and `Pillow` libraries. You can install these dependencies using `pip install -r requirements.txt`.

## How to use Ytrojan

### Run `src/main_cli.py` using Python 3.10 or higher interpreter
    __   ___             _             ____  
    \ \ / / |_ _ __ ___ (_) __ _ _ __ |___ \ 
     \ V /| __| '__/ _ \| |/ _` | '_ \  __) |
      | | | |_| | | (_) | | (_| | | | |/ __/ 
      |_|  \__|_|  \___// |\__,_|_| |_|_____|
                      |__/   

### Command Introduction

#### 1. generate command

Format: `generate <host> <port> <path>`
API: `control.generate(host:str,port:str,path:str) -> None`
This command is used to generate a malicious Python script on the bot side. `host` and `port` are the addresses for the control side, and `path` is the save path for the generated script.

#### 2. service command

Format: `service <host> <port>`
API: `control.serice(socket:socket.socket) -> None`
This command is used to start a child thread to handle bot connections. `host` and `port` are the addresses for the control side.

#### 3. listbot command

Format: `botlist`
This command is used to output the bots currently connected to the control, displaying bot ID and network address.

#### 4. sysinfo command

Format: `sysinfo <id>`
API: `control.sysinfo(socket:socket.socket) -> dict`
This command is used to output detailed information about the bot, including the operating system, network name, hardware information, etc.

#### 5. shell command

Format: `shell <id> <command>`
API: `control.shell(socket:socket.socket,input:list[str],timeout:bool) -> tuple`
This command is used to execute a shell command on the bot.

Note that the `timeout` parameter in `control.shell` determines whether to enable timeout handling when using the `shell` command.

#### 6. shell_nt command

Format: `shell_nt <id> <command>`
API: `control.shell(socket:socket.socket,input:list[str],timeout:bool) -> tuple`
This command is the same as the previous one but does not enable timeout handling.

#### 7. script command

Format: `script <id> <path>`
API: `control.script(socket:socket.socket,local_path:str) -> tuple`
This command is used to remotely execute a Python script on the bot side.

#### 8. download command

Format: `download <id> <remote_path> <local_path>`
API: `control.download(socket:socket.socket,remote_path:str,local_path:str) -> bool`
This command downloads a file to the local machine. Note that both `remote_path` and `local_path` should point to a file, not a directory.

#### 9. upload command

Format: `upload <id> <local_path> <remote_path>`
API: `control.upload(socket:socket.socket,local_path:str,remote_path:str) -> bool`
This command uploads a file to the bot. Note that both `remote_path` and `local_path` should point to a file, not a directory.

#### 10. screenshot command

Format: `screenshot <id> <path>`
API: `screenshot(socket:socket.socket,local_path:str) -> bool`
This command takes a screenshot on the bot and saves it locally. The `local_path` should point to a file, not a directory.

#### 11. webcamlist command

Format: `webcamlist <id>`
API: `control.webcamlist(socket:socket.socket) -> tuple`
This command retrieves a list of available webcams on the bot and their dimensions.

#### 12. webcamsnap command

Format: `webcamsnap <id> <index> <path>`
API: `webcamsnap(socket:socket.socket,id:int,local_path:str) -> bool`
This command calls the specified webcam on the bot to take a photo and saves it locally. The `local_path` should point to a file, not a directory.

#### 13. kill command

Format: `kill <id>`
API: `control.kill(id:int) -> None`
This command is used to terminate the bot connection.

#### 14. exit command

Format: `exit`
Command to exit.

## Final Notes   

As you can see, Ytrojan currently has limited functionality. We don't have features like anti-detection modules, privilege escalation, or pivoting to penetrate internal networks. At the moment, Ytrojan is more like a toy created by a junior high school student.

Ytrojan may stop receiving updates for a long time as I am now in the third year of junior high school, and my grades are not good. During this period, if you have good ideas, you can submit a pull request, and I will be very grateful!   

Translation by ChatGPT
