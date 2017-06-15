from Tkinter import *
import tkFont


#Testframe = Frame(root)
#Testframe.pack()
## defines the typing function so as the user can type into the program
#bold = False
#underlined = False
#italics = False

class menuClass(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.bold = False
		self.underlined = False
		self.italics = False
		self.familyFont = "arial"
		self.textSize = 18
		print str(self.underlined)
		#self.dFont = tkFont.Font(family = "Helvetica", size=10)
		dFont = tkFont.Font(family = self.familyFont, size = self.textSize)
		self.lb = Text(self, width=16, height=5, font = dFont)
		self.lb.pack(side = LEFT, fill=BOTH, expand = YES)
		self.yscrollbar = Scrollbar(self, orient=VERTICAL, command=self.lb.yview)
		self.yscrollbar.pack(side=RIGHT, fill=Y)
		self.lb["yscrollcommand"] = self.yscrollbar.set 
		menubar = Menu(self)
		filemenu = Menu(menubar, tearoff =0)
		filemenu.add_command(label="New", command= lambda : self.donothing())
		filemenu.add_command(label="Open", command=lambda:self.donothing())
		filemenu.add_command(label="Save", command=lambda:self.donothing())
		filemenu.add_command(label="Save as...", command=lambda:self.donothing())
	
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=Tk.quit)
		
		menubar.add_cascade(label="File", menu=filemenu)
		editmenu = Menu(menubar, tearoff=0)
		editmenu.add_command(label="Undo", command=lambda:self.donothing())
	
		editmenu.add_separator()
	
		editmenu.add_command(label="Cut", command=lambda:self.donothing())
		editmenu.add_command(label="Copy", command=lambda:self.copy())
		editmenu.add_command(label="Paste", command=lambda:self.paste())
		editmenu.add_command(label="Delete", command=lambda:self.delete())
		editmenu.add_command(label="Select All", command=lambda:self.donothing())
	
		formatmenu = Menu(menubar, tearoff=0)
		formatmenu.add_command(label="Tab", command=lambda:self.donothing())
	
		menubar.add_cascade(label="Edit", menu=editmenu)
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help Index", command=lambda:self.donothing())
		helpmenu.add_command(label="About...", command=lambda:self.donothing())
		menubar.add_cascade(label="Help", menu=helpmenu)
		menubar.add_cascade(label="Format", menu=formatmenu)
			
		Testframe = Frame(self)
		Testframe.pack()
		B = Button(Testframe, text ="B", width = 1, padx = -4, command = lambda:self.bolded())
		U = Button(Testframe, text ="U", width = 1, padx = -4, command = lambda:self.underlines())
		I = Button(Testframe, text ="I", width = 1, padx = -4, command = lambda:self.intalicised())
	
		I.pack(side = TOP, fill = X)#grid(row = 0, column = 0) #Displays the button with a position 0, 0
		U.pack(side = TOP, fill = X)#grid(row = 0, column = 1) #Row is verticle position, column is horizontal
		B.pack(side = TOP, fill = X)#grid(row = 0, column = 2)
		self.config(menu=menubar)
	
	def donothing(self):
		filewin = Toplevel(root)
		button = Button(filewin, text = "Do nothing!!")
		button.pack()
		
	content = ""
	def copy(self):
		self.clipboard_clear()
		start = self.lb.index('sel.first')
		end = self.lb.index('sel.last')
		textCopy = self.lb.get(start, end)
		self.clipboard_append(textCopy)
	def paste(self):
		# get the clipboard data, and replace all newlines
		# with the literal string "\n"
		clipboard = self.clipboard_get()
		clipboard = clipboard.replace("\n", "\\n")
		
		# delete the selected text, if any
		try:
			start = self.lb.index('sel.first')
			end = self.lb.index('sel.last')
			self.lb.delete(start, end)
		except TclError, e:
			pass #nothing was selected, so paste doesn't need to delete anything
		
		# insert the modified clipboard contents
		self.lb.insert("insert", clipboard)
	def delete(self):
		try:
			start = self.lb.index("sel.first")
			end = self.lb.index("sel.last")
			self.lb.delete(start, end)
		except TclError, e:
			pass
	def bolded(self):
		if self.bold == False:
			self.bold = True
			self.conditions()
		elif self.bold == True:
			self.bold = False
			self.conditions()
	def intalicised(self):
		if self.italics == False:
			self.italics = True
			self.conditions()
		elif self.italics == True:
			self.italics = False
			self.conditions()
	def underlines(self):
		if self.underlined == False:
			self.underlined = True
			#print str(self.underlined)
			self.conditions()
		elif self.underlined == True:
			self.underlined = False
			#print str(self.underlined)
			self.conditions()
			
	def conditions(self):
		if (self.bold == True and self.italics == False and self.underlined == False):
			aFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold')
			self.lb = Text(self, width=16, height=5, font = aFont)
		elif (self.bold == False and self.italics == True and self.underlined == False):
			bFont = tkFont.Font(family = self.familyFont, size = self.textSize, slant = 'italic')
			self.lb = Text(self, width=16, height=5, font = bFont)
		elif (self.bold == False and self.italics == False and self.underlined == True):
			print "It's working!"
			cFont = tkFont.Font(family = self.familyFont, size = self.textSize, underline = True)
			self.lb = Text(self, width=16, height=5, font = cFont)
		elif (self.bold == True and self.italics == True and self.underlined == False):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', slant = 'italic')
			self.lb = Text(self, width=16, height=5, font = dFont)
		elif (self.bold == False and self.italics == True and self.underlined == True):
			eFont = tkFont.Font(family = self.familyFont, size = self.textSize, slant = 'italic', underline = True)
			self.lb = Text(self, width=16, height=5, font = eFont)
		elif (self.bold == True and self.italics == False and self.underlined == True):
			fFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', underline = True)
			self.lb = Text(self, width=16, height=5, font = fFont)
		elif (self.bold == True and self.italics == True and self.underlined == True):
			gFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', slant = 'italic', underline = True)
			self.lb = Text(self, width=16, height=5, font = gFont)
		elif (self.bold == False and self.italics == False and self.underlined == False):
			print "Testing woot"
			hFont = tkFont.Font(family = self.familyFont, size = self.textSize)
			self.lb = Text(self, width=16, height=5, font = hFont)
if __name__ == "__main__":
    app = menuClass()
    #menuClass().conditions()
    app.mainloop()

