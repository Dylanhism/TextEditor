from Tkinter import *
import tkFont

root = Tk()
#Testframe = Frame(root)
#Testframe.pack()
## defines the typing function so as the user can type into the program

class menuClass(root):
	def __init__(self, *args, **kwargs):
		root.__init__(self, *args, **kwargs)
		self.dFont = tkFont.Font(family = "Helvetica", size=10)
		self.lb = Text(root, width=16, height=5, font=self.dFont)
		self.lb.pack(side = LEFT, fill=BOTH, expand = YES)
		self.yscrollbar = Scrollbar(root, orient=VERTICAL, command=self.lb.yview)
		self.yscrollbar.pack(side=RIGHT, fill=Y)
		self.lb["yscrollcommand"] = self.yscrollbar.set 
	def menus(self):
		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff =0)
		filemenu.add_command(label="New", command= lambda : donothing())
		filemenu.add_command(label="Open", command=lambda:donothing())
		filemenu.add_command(label="Save", command=lambda:donothing())
		filemenu.add_command(label="Save as...", command=lambda:donothing())
	
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=root.quit)
		
		menubar.add_cascade(label="File", menu=filemenu)
		editmenu = Menu(menubar, tearoff=0)
		editmenu.add_command(label="Undo", command=lambda:donothing())
	
		editmenu.add_separator()
	
		editmenu.add_command(label="Cut", command=lambda:donothing())
		editmenu.add_command(label="Copy", command=lambda:copy())
		editmenu.add_command(label="Paste", command=lambda:paste())
		editmenu.add_command(label="Delete", command=lambda:donothing())
		editmenu.add_command(label="Select All", command=lambda:donothing())
	
		formatmenu = Menu(menubar, tearoff=0)
		formatmenu.add_command(label="Tab", command=lambda:donothing())
	
		menubar.add_cascade(label="Edit", menu=editmenu)
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help Index", command=lambda:donothing())
		helpmenu.add_command(label="About...", command=lambda:donothing())
		menubar.add_cascade(label="Help", menu=helpmenu)
		menubar.add_cascade(label="Format", menu=formatmenu)
			
		Testframe = Frame(root)
		Testframe.pack()
		B = Button(Testframe, text ="B", width = 1, padx = -4, command = lambda:donothing())
		U = Button(Testframe, text ="U", width = 1, padx = -4, command = lambda:donothing())
		I = Button(Testframe, text ="I", width = 1, padx = -4, command = lambda:donothing())
	
		I.pack(side = TOP, fill = X)#grid(row = 0, column = 0) #Displays the button with a position 0, 0
		U.pack(side = TOP, fill = X)#grid(row = 0, column = 1) #Row is verticle position, column is horizontal
		B.pack(side = TOP, fill = X)#grid(row = 0, column = 2)
		root.config(menu=menubar)
	
	def donothing(self):
		filewin = Toplevel(root)
		button = Button(filewin, text = "Do nothing!!")
		button.pack()
		
	content = ""
	def copy(self):
		global content
		content = self.lb.get(SEL_FIRST, SEL_LAST)
		print content
	def paste(self):
		clipboard = self.clipboard_get()
		pasteValue = content
		self.lb.insert("insert", clipboard)


menuClass(root).mainloop()
