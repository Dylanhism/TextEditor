import Tkinter as tk
from Tkinter import TclError

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, width=40, height=8)
        self.button = tk.Button(self, text="do it!", command=self.doit)
        self.button.pack(side="top")
        self.text.pack(side="bottom", fill="both", expand=True)
        self.doit()

    def doit(self, *args):
        # get the clipboard data, and replace all newlines
        # with the literal string "\n"
        clipboard = self.clipboard_get()
        clipboard = clipboard.replace("\n", "\\n")

        # delete the selected text, if any
        try:
            start = self.text.index("sel.first")
            end = self.text.index("sel.last")
            self.text.delete(start, end)
        except TclError, e:
            # nothing was selected, so paste doesn't need
            # to delete anything
            pass

        # insert the modified clipboard contents
        self.text.insert("insert", clipboard)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
