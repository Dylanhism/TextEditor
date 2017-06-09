from Tkinter import *
import tkFont

class Texty(object):
	def __init__(self, familyFont, textSize, root ):
		self.root = root 
		self.familyFont = familyFont
		self.textSize = textSize

	def text (self):
		dFont=tkFont.Font(family = self.familyFont, size = self.textSize )
		lb=Text(self.root, width=16, height=5, font=dFont)
		lb.pack(side=LEFT, fill=BOTH, expand = YES)
		yscrollbar=Scrollbar(self.root, orient=VERTICAL, command=lb.yview)
		yscrollbar.pack(side=RIGHT, fill=Y)
		lb["yscrollcommand"]=yscrollbar.set
root = Tk()

Texty(familyFont, textSize, root).text()


root.mainloop()
