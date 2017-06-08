from Tkinter import *
import tkFont

##class Texty(object):
##	def __init__(self, family):
##		self.textFont = family


def killme():
	root.quit()
        root.destroy()
root=Tk()
family = "Arial"
##def text (textfont):
dFont=tkFont.Font(family = "Helvetica bold", size=10)
lb=Text(root, width=16, height=5, font=dFont)
lb.pack(side=LEFT, fill=BOTH, expand = YES)
yscrollbar=Scrollbar(root, orient=VERTICAL, command=lb.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
lb["yscrollcommand"]=yscrollbar.set
##text(family)
root.mainloop()
