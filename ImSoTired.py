from Tkinter import *
import tkFont
## imports tk file dialog which allows you to access different file options such as save and open
import tkFileDialog

class menuClass(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.bold = False
        self.underlined = False
        self.italics = False
        self.clearText = False
        self.familyFont = "arial"
        self.textSize = 18
        self.dFont = tkFont.Font(family = self.familyFont, size = self.textSize)
        self.lb = Text(self, width=16, height=5, font = self.dFont)
        self.lb.pack(side = LEFT, fill=BOTH, expand = YES)
        self.yscrollbar = Scrollbar(self, orient=VERTICAL, command=self.lb.yview)
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.lb["yscrollcommand"] = self.yscrollbar.set 
        
        self.boldFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = "bold")
        self.lb.tag_configure("BOLD", font = self.boldFont)
        self.italicsFont = tkFont.Font(family = self.familyFont, size = self.textSize, slant = 'italic')
        self.lb.tag_configure("ITALICS", font = self.italicsFont)
        self.underlineFont = tkFont.Font(family = self.familyFont, size = self.textSize, underline = True)
        self.lb.tag_configure("UNDERLINE", font = self.underlineFont)
        self.boldItalics = tkFont.Font(family=self.familyFont, size=self.textSize, weight = 'bold', slant = 'italic')
        self.lb.tag_configure("BOLDITALICS", font = self.boldItalics)
        self.boldUnder = tkFont.Font(family=self.familyFont, size=self.textSize, weight = 'bold', underline = True)
        self.lb.tag_configure("BOLDUNDER", font = self.boldUnder)
        self.italicsUnder = tkFont.Font(family = self.familyFont, size = self.textSize, slant = 'italic', underline = True)
        self.lb.tag_configure("ITALICSUNDER", font = self.italicsUnder)
        self.allFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', slant = 'italic', underline = True)
        self.lb.tag_configure("ALLFONT", font = self.allFont)
        
        
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff =0)
        filemenu.add_command(label="New", command= lambda : self.newFile())
        filemenu.add_command(label="Open", command=lambda:self.fileStuff())
        filemenu.add_command(label="Save", command=lambda:self.save_as_file())
        filemenu.add_command(label="Save as...", command=lambda:self.save_as_file())

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=lambda:self.cut())
        editmenu.add_command(label="Copy", command=lambda:self.copy())
        editmenu.add_command(label="Paste", command=lambda:self.paste())
        editmenu.add_command(label="Delete", command=lambda:self.delete())

        formatmenu = Menu(menubar, tearoff=0)
        formatmenu.add_command(label="8", command=lambda:self.getSize(8))

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Format", menu=formatmenu)
        
        
        filemenu.add_separator()

        fontsmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "fonts", menu = fontsmenu)

        fontsmenu.add_command(label = "8", command = lambda:donothing())
        fontsmenu.add_command(label = "9", command = lambda:donothing())
        fontsmenu.add_command(label = "10", command = lambda:donothing())
        fontsmenu.add_command(label = "11", command = lambda:donothing())
        fontsmenu.add_command(label = "12", command = lambda:donothing())
        fontsmenu.add_command(label = "14", command = lambda:donothing())
        fontsmenu.add_command(label = "18", command = lambda:donothing())
        fontsmenu.add_command(label = "24", command = lambda:donothing())


		filemenu.add_separator()

		sizesmenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "sizes", menu = sizesmenu)
		
		sizesmenu.add_command(label = "8", command = lambda:donothing())
		sizesmenu.add_command(label = "9", command = lambda:donothing())
		sizesmenu.add_command(label = "10", command = lambda:donothing())
		sizesmenu.add_command(label = "11", command = lambda:donothing())
		sizesmenu.add_command(label = "12", command = lambda:donothing())
		sizesmenu.add_command(label = "14", command = lambda:donothing())
		sizesmenu.add_command(label = "18", command = lambda:donothing())
        sizesmenu.add_command(label = "24", command = lambda:donothing())
        
        
        Testframe = Frame(self)
        Testframe.pack()
        B = Button(Testframe, text ="B", width = 1, padx = -4, command = lambda:self.bolded())
        U = Button(Testframe, text ="U", width = 1, padx = -4, command = lambda:self.underlines())
        I = Button(Testframe, text ="I", width = 1, padx = -4, command = lambda:self.intalicised())
        BI =Button(Testframe, text="BI", width = 1, padx = -4, command = lambda:self.boldItalicsF())
        IU =Button(Testframe, text="IU", width = 1, padx = -4, command = lambda:self.italicsUnderlined())
        BU =Button(Testframe, text="BU", width = 1, padx = -4, command = lambda:self.boldUnderlined())
        BUI=Button(Testframe, text="A",width = 1, padx = -4, command = lambda:self.allFormat())
        x = Button(Testframe, text="X", width = 1, padx = -4, command = lambda:self.clear())

        I.pack(side = TOP, fill = X)#grid(row = 0, column = 0) #Displays the button with a position 0, 0
        U.pack(side = TOP, fill = X)#grid(row = 0, column = 1) #Row is verticle position, column is horizontal
        B.pack(side = TOP, fill = X)#grid(row = 0, column = 2)
        BI.pack(side = TOP)
        BU.pack(side = TOP)
        IU.pack(side = TOP)
        BUI.pack(side = TOP)
        x.pack(side = TOP)
        self.config(menu=menubar)
    
    def donothing(self):
        filewin = Toplevel(root)
        button = Button(filewin, text = "Coming in future updates!!")
        button.pack()
    def getSize(self, number):
        self.textSize = number
        print self.textSize
    content = ""
    def cut(self):
        self.copy()
        self.delete()
    def newFile(self):
        self.lb.delete('1.0', 'end')
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

    ## function for save as file so that it can be called by command buttons
    def save_as_file(self):
        ## takes the name of the file and saves it as default to a .txt file
        name = tkFileDialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
        ## if the user cancels the save before it finishes then returns back to the main function without any errors
        if name is None:
                return
        ## gets the index for the text file
        text2save = str(self.lb.get(1.0, END))
        ## writes to the name file all of the index in text2save
        name.write(text2save)
        ##closes the file 
        name.close()
    def fileStuff (self):
        self.newroot = Tk()
        tWlabel = Label(self.newroot, text= "Please enter your file name exaclty and press done")
        tWlabel.pack()
        self.tW = Text(self.newroot, height=1, width=50)
        self.tW.pack()
        twButton = Button(self.newroot, text="Done", command = lambda:self.filePaste())
        twButton.pack()

    def filePaste (self):
        self.filename = self.tW.get(1.0, END)
        self.filename = self.filename[:-1]
        data_file = open(self.filename)
        data = data_file.read()
        self.lb.insert(END, data)
        self.newroot.destroy()

    
    def bolded(self):
        self.bold = True
        self.conditions()
        self.bold = False
    def intalicised(self):
        self.italics = True
        self.conditions()
        self.italics = False
    def underlines(self):
        self.underlined = True
        self.conditions()
        self.underlined = False
    def boldItalicsF(self):
        self.bold = True
        self.italics = True
        self.conditions()
        self.bold = False
        self.italics = False
    def italicsUnderlined(self):
        self.italics = True
        self.underlined = True
        self.conditions()
        self.italics = False
        self.underlined = False
    def boldUnderlined(self):
        self.bold = True
        self.underlined = True
        self.conditions()
        self.bold = False
        self.underlined = False
    def clear(self):
        self.clearText = True
        self.conditions()
        self.clearText = False
    def allFormat(self):
        self.bold = True
        self.italics = True
        self.underlined = True
        self.conditions()
        self.bold = False
        self.italics = False
        self.underlined = False
    def conditions(self):
        if (self.bold == True and self.italics == False and self.underlined == False):
            try:
                self.lb.tag_add("BOLD", "sel.first", 'sel.last')
                print self.lb.tag_names()
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
                #self.bold = False
            except TclError:
                pass
        elif (self.bold == False and self.italics == True and self.underlined == False):
            try:
                self.lb.tag_add("ITALICS", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
                #self.italics = False
            except TclError:
                pass
        elif (self.bold == False and self.italics == False and self.underlined == True):
            try:
                self.lb.tag_add("UNDERLINE", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
                #self.underlined = False
            except TclError:
                pass
        elif (self.bold == True and self.italics == True and self.underlined == False):
            try:
                self.lb.tag_add("BOLDITALICS", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
            except TclError:
                pass
        elif (self.bold == False and self.italics == True and self.underlined == True):
            try:
                self.lb.tag_add("ITALICSUNDER", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDITALICS", "sel.first", 'sel.last')
            except TclError:
                pass
        elif (self.bold == True and self.italics == False and self.underlined == True):
            try:
                self.lb.tag_add("BOLDUNDER", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
            except TclError:
                pass
        elif (self.bold == True and self.italics == True and self.underlined == True):
            try:
                self.lb.tag_add("ALLFONT", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
            except TclError:
                pass
        elif (self.clearText == True):
            try:
                self.lb.tag_remove("ALLFONT", "sel.first", "sel.last")
                self.lb.tag_remove("BOLDITALICS", "sel.first", "sel.last")
                self.lb.tag_remove("BOLD", "sel.first", 'sel.last')
                self.lb.tag_remove("UNDERLINE", "sel.first", 'sel.last')
                self.lb.tag_remove("BOLDUNDER", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICS", "sel.first", 'sel.last')
                self.lb.tag_remove("ITALICSUNDER", "sel.first", 'sel.last')
            except TclError:
                pass
if __name__ == "__main__":
    app = menuClass()
    #menuClass().conditions()
    app.mainloop()
