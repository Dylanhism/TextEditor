from Tkinter import *
## imports tk file dialog which allows you to access different file options such as save and open
import tkFileDialog

## function for save as file so that it can be called by command buttons
def save_as_file():
	## takes the name of the file and saves it as default to a .txt file
	name = tkFialDialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
	## if the user cancels the save before it finishes then returns back to the main function without any errors
	if name is None:
		return
`	## gets the index for the text file
	text2save = str(text.get(1.0, END))
	## writes to the name file all of the index in text2save
	name.write(text2save)
	##closes the file 
	name.close()
