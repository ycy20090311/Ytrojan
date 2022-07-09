import Generate

if "__main__" == __name__:
    print("""
     _____ _     _         _   _   _                 _ 
    |_   _| |__ (_)_ __ __| | | | | | __ _ _ __   __| |
      | | | '_ \| | '__/ _` | | |_| |/ _` | '_ \ / _` |
      | | | | | | | | | (_| | |  _  | (_| | | | | (_| |
      |_| |_| |_|_|_|  \__,_| |_| |_|\__,_|_| |_|\__,_|
                                                    
                                            V 0.1
    """)

    while True:
        cmd = input("Third-Hand $>").split()
        if cmd[0] == "generate":
          Generate.generate(int(cmd[1]),cmd[2],(cmd[3],int(cmd[4])))
        elif cmd[0] == "connect":
          Generate.connect((cmd[1],int(cmd[2])))
        elif cmd[0] == "listen":
          Generate.listen((cmd[1],int(cmd[2])))
        elif cmd[0] == "exit":
          exit()
        else:
          print("Third-Hand不包含%s命令" % cmd[0])


