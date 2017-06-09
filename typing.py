from Tkinter import *
import tkFont

root = Tk()
Testframe = Frame(root)
Testframe.pack()
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
		
	Testframe = Frame(root)
	Testframe.pack()
	B = Button(Testframe, text ="B", width = 1, padx = -4, command = donothing)
	U = Button(Testframe, text ="U", width = 1, padx = -4, command = donothing)
	I = Button(Testframe, text ="I", width = 1, padx = -4, command = donothing)

	I.pack(side = TOP, fill = X)#grid(row = 0, column = 0) #Displays the button with a position 0, 0
	U.pack(side = TOP, fill = X)#grid(row = 0, column = 1) #Row is verticle position, column is horizontal
	B.pack(side = TOP, fill = X)#grid(row = 0, column = 2)
	root.config(menu=menubar)
        
##def text (textfont):
dFont = tkFont.Font(family = "Helvetica", size=10)
lb = Text(root, width=16, height=5, font=dFont)
lb.pack(side = LEFT, fill=BOTH, expand = YES)
yscrollbar = Scrollbar(root, orient=VERTICAL, command=lb.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
lb["yscrollcommand"] = yscrollbar.set 

menus()
root.mainloop()

        
        
        
        

