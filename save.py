from Tkinter import *
import tkFileDialog

def save_as_file():
	name = tkFialDialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
	if name is None:
		return

	text2save = str(text.get(1.0, END))
	name.write(text2save)
	f.close()
