from os import name
from tkinter import *
from tkinter import font 
from tkinter import ttk

class PythonPDFTools:

  def __init__(self, root):
    self.root = root
    self.frame = ttk.Frame(self.root, padding=10)
    self.fntTitle = font.Font(family="Helvetica", name="appFntTitle", size=32, weight="bold")
    self.lblTitle = ttk.Label(self.frame, text="PyDF Tools", font=self.fntTitle)
    self.btnMerge = ttk.Button(self.frame, text="Merge PDFs", command=self.openMerge)
    self.lblTitle.pack()
    self.btnMerge.pack()
    self.frame.pack()

  def openMerge(self):
    self.newWindow = Toplevel(self.root)
    self.app = MergePDFs(self.newWindow)
    
class MergePDFs:
  def __init__(self, parent):
    self.parent = parent
    self.frame = ttk.Frame(self.parent, padding=10)
    self.frame.pack()
    

root = Tk()
PythonPDFTools(root)
root.mainloop()

