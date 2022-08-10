from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
# from cv2 import SIFT
# from sklearn.linear_model import Ridge
from inventory import *
from tkinter import ttk,messagebox

class recordclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+300+130")
        self.root.title("INVENTORY MANAGEMENT SYSTEM | PADMAVATI")
        self.root.config(bg="#FFDFDD")
        self.root.focus_force()
    
        rcd_frame=Frame(self.root,bd=3,relief=RIDGE)
        rcd_frame.place(x=0,y=0,relwidth=1,relheight=1)

        scrolly=Scrollbar(rcd_frame,orient=VERTICAL)
        scrollx=Scrollbar(rcd_frame,orient=HORIZONTAL)

        self.table=ttk.Treeview(rcd_frame,column=("pid","desc","ql","qp","loc","supp"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)

        self.table.heading("pid",text="Product ID")
        self.table.heading("desc",text="Description")
        self.table.heading("ql",text="Quantity Loose")
        self.table.heading("qp",text="Quantity Packet")
        self.table.heading("loc",text="Location")
        self.table.heading("supp",text="Supplier")
        self.table["show"]="headings"

        self.table.column("pid",width=100)
        self.table.column("desc",width=100)
        self.table.column("ql",width=100)
        self.table.column("qp",width=100)
        self.table.column("loc",width=100)
        self.table.column("supp",width=100)

        self.table.pack(fill=BOTH,expand=1)

#=============================================================================

        





if __name__=="__main__":
    root=Tk()
    obj=recordclass(root)
    root.mainloop()