from Tkinter import *
root = Tk()
mainFrame = Frame(root)
mainFrame.grid()
entryFrame = Frame(mainFrame, width=454, height=20)
entryFrame.grid(row=0, column=1)    
entryFrame.columnconfigure(0, weight=10)  
entryFrame.grid_propagate(False)
## defines the typing function so as the user can type into the program
def typing(event):
    cur_cursor = text.index("insert")
    text.tag_add('note', cur_cursor + '-1c', cur_cursor)
    text.tag_add('note2', cur_cursor, cur_cursor + '+1c')
 
text = Text(root)
text.grid()
text.bind('<KeyRelease>', typing)

root.mainloop()


