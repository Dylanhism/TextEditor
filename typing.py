from Tkinter import *
import tkFont

root = Tk()
mainFrame = Frame(root)
mainFrame.grid()
entryFrame = Frame(mainFrame, width=454, height=20)
entryFrame.grid(row=0, column=1)
entryFrame.columnconfigure(0, weight=10)
entryFrame.grid_propagate(False)
## defines the typing function so as the user can type into the program
def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text = "Do nothing!!")
        button.pack()
def menus():
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff =0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        formatmenu = Menu(menubar, tearoff=0)
        formatmenu.add_command(label="Tab", command=donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        menubar.add_cascade(label="Format", menu=formatmenu)


        B = Button(root, text ="B", width = 1, padx = -4, command = donothing)
        U = Button(root, text ="U", width = 1, padx = -4, command = donothing)
        I = Button(root, text ="I", width = 1, padx = -4, command = donothing)

        I.grid(row = 0, column = 0) #Displays the button with a position 0, 0
        U.grid(row = 0, column = 1) #Row is verticle position, column is horizontal
        B.grid(row = 0, column = 2)
        root.config(menu=menubar)
        
family = "Arial"
##def text (textfont):
dFont=tkFont.Font(family = "Helvetica bold", size=10)
lb=Text(root, width=16, height=5, font=dFont)
lb.pack(side=LEFT, fill=BOTH, expand = YES)
yscrollbar=Scrollbar(root, orient=VERTICAL, command=lb.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
lb["yscrollcommand"]=yscrollbar.set

menus()
root.mainloop()

        
        
        
        

