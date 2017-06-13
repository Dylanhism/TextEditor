## imports everything from tkinter
from Tkinter import *
## imports the fonts for tkinter
import tkFont

## makes class 
class Texty(object):
	def __init__(self, familyFont, textSize, root ):
		self.root = root 
		self.familyFont = familyFont
		self.textSize = textSize

	def text (self):
		if (bold == True and italics == False and underlines == False):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold')
		elif (bold == False and italics == True and underlines == False):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, slant = 'italic')
		elif (bold == False and italics == False and underlines == True):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, underline = True)
		elif (bold == True and italics == True and underlines == False):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', slant = 'italic')
		elif (bold == False and italics == True and underlines == True):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, slant = 'italic', underline = True)
		elif (bold == True and italics == False and underlines == True):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', underline = True)
		elif (bold == True and italics == True and underlines == True):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize, weight = 'bold', slant = 'italic', underline = True)
		elif (bold == False and italics == False and underlines == False):
			dFont = tkFont.Font(family = self.familyFont, size = self.textSize)


		lb=Text(self.root, width=16, height=5, font=dFont)
		lb.pack(side=LEFT, fill=BOTH, expand = YES)
		yscrollbar=Scrollbar(self.root, orient=VERTICAL, command=lb.yview)
		yscrollbar.pack(side=RIGHT, fill=Y)
		lb["yscrollcommand"]=yscrollbar.set
root = Tk()

bold = False
italics = False
underlines = False
familyFont = "arial"
textSize = 50



Texty(familyFont, textSize, root).text()


root.mainloop()
