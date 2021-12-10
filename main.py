from tkinter import *
from tkinter import font 
from tkinter import ttk
from tkinter import filedialog

import PyDF2 as pdf

class PythonPDFTools:

  def __init__(self, root):
    self.root = root
    self.root.title("PyDF Tools")
    self.frame = ttk.Frame(self.root, padding=10)
    self.fntTitle = font.Font(family="Helvetica", name="appFntTitle", size=32, weight="bold")
    self.lblTitle = ttk.Label(self.frame, text="PyDF Tools", font=self.fntTitle)
    self.btnMerge = ttk.Button(self.frame, text="Merge PDFs", command=self.openMerge)
    self.lblTitle.pack()
    self.btnMerge.pack()
    self.frame.pack()

  def openMerge(self):
    self.newWindow = Toplevel(self.root)
    self.newWindow.attributes('-topmost', 1)
    self.app = MergePDFs(self.newWindow)
    
class MergePDFs:
  def __init__(self, parent):
    self.parent = parent
    self.parent.title("Merge PDFs")
    self.frame = ttk.Frame(self.parent, padding=10)
    self.path = [StringVar(), StringVar()]

    self.lblDirections = ttk.Label(self.frame, text="Select 2 PDFs to merge.")
    self.lblDirections.grid(column=0, row=0, columnspan=2)

    _entry = lambda index: ttk.Entry(self.frame, textvariable=self.path[index])
    _browse = lambda index: ttk.Button(self.frame, text="Browse", command=lambda : self.openFile(index))

    self.entryPath1 = _entry(0)
    self.entryPath1.grid(column=0, row=1, sticky="NSEW") 
    self.btnBrowse1 = _browse(0)
    self.btnBrowse1.grid(column=1, row=1, sticky="NSWE")  

    self.entryPath2 = ttk.Entry(self.frame, textvariable=self.path[1])
    self.entryPath2.grid(column=0, row=2, sticky="NSEW") 
    self.btnBrowse2 = _browse(1)
    self.btnBrowse2.grid(column=1, row=2, sticky="NSWE")

    self.btnMerge = ttk.Button(self.frame, text="Merge", command=self.merge)

    self.frame.pack(fill=BOTH, expand=1)

    self.frame.grid_columnconfigure(0, weight=1)
    self.frame.grid_columnconfigure(1, weight=0)

    # self.frame.grid_rowconfigure(0, weight=1)
    # self.frame.grid_rowconfigure(1, weight=1)
    # self.frame.grid_rowconfigure(2, weight=1)

  def openFile(self, entryIndex):
    filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
    self.path.append(StringVar())
    file = filedialog.askopenfilename(title="Select PDF", initialdir='./', filetypes=filetypes)
    print(file)
    self.path[entryIndex].set(file)

  def merge(self):
    with open(self.path[0], 'rb') as f1, open(self.path[1], 'rb') as f2:
      pdf1 = pdf.PdfFileReader(f1)
      pdf2 = pdf.PdfFileReader(f2)
      writer = pdf.PdfFileWriter()

      for page in range(pdf1.numPages):
        pageObj = pdf1.getPage(page)
        writer.addPage(pageObj)

      for page in range(pdf2.numPages):
        pageObj = pdf2.getPage(page)
        writer.addPage(pageObj)

      output = open()
    

root = Tk()
PythonPDFTools(root)
root.mainloop()

