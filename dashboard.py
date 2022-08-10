from tkinter import*
from PIL import Image,ImageTk
from record import recordclass
from inventory import inventoryclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+5+5")
        self.root.title("INVENTORY MANAGEMENT SYSTEM | PADMAVATI")
        self.root.config(bg="#FFDFDD")

        #-------title----S--
        self.icon_title=PhotoImage(file="dashboard\cartpng.png")
        title=Label(self.root,text="Inventory Management System | PADMAVATI",image=self.icon_title,compound=LEFT,font=("times new roman",35,"bold"),bg="#1569C7",fg="white",anchor="w",padx=100) ##1569C7='Blue eyes'
        title.place(x=0,y=0,relwidth=1,height=70)

        #-------Log Out------
        btn_logout=Button(self.root,text="Log Out",font=("times new roman",20,"bold"),bg="#E3E4FA",fg="black",anchor="e",padx=20,cursor="hand2") ##E3E4FA='Lavender Blue' 
        btn_logout.place(x=1300,y=10,height=50,width=150)

        #------clock------
        self.lbl_clock=Label(self.root,text="Welcome to Padmavati\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white") 
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #------LEFT MENU--------
        self.Menulogo=Image.open("dashboard\logo.png")
        self.Menulogo=self.Menulogo.resize((200,200),Image.ANTIALIAS)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)

        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=120,width=200,height=650)

        lbl_menulogo=Label(leftmenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        lbl_menu=Label(leftmenu,text="Menu",font=("times new roman",20),bg="#009688")
        lbl_menu.pack(side=TOP,fill=X)

        #----Button in left menu----
        self.icon_inv=PhotoImage(file="dashboard\point1.png")
        btn_inventory=Button(leftmenu,text="Inventory",command=self.inventory,image=self.icon_inv,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_inventory.pack(side=TOP,fill=X)

        btn_inventory=Button(leftmenu,text="Record",command=self.record,image=self.icon_inv,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_inventory.pack(side=TOP,fill=X)
        
        btn_inventory=Button(leftmenu,text="Product",image=self.icon_inv,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_inventory.pack(side=TOP,fill=X)
        
        btn_inventory=Button(leftmenu,text="Supplier",image=self.icon_inv,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_inventory.pack(side=TOP,fill=X)
        
        btn_inventory=Button(leftmenu,text="Sales",image=self.icon_inv,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_inventory.pack(side=TOP,fill=X)
        
        btn_inventory=Button(leftmenu,text="Exit",image=self.icon_inv,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2")
        btn_inventory.pack(side=TOP,fill=X)
        
        #---content---
        self.lbl_inv=Label(self.root,text="Total Storage\n[0]",bd=5,relief=RIDGE,bg="#1589FF",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_inv.place(x=300,y=120,height=150,width=300)

        # self.lbl_inv=Label(self.root,text="Total employee\n[0]",bd=5,relief=RIDGE,bg="#7F38EC",fg="white",font=("goudy old style",20,"bold"))
        # self.lbl_inv.place(x=650,y=120,height=150,width=300)

        self.lbl_inv=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#31906E",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_inv.place(x=650,y=120,height=150,width=300)

        self.lbl_inv=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#C04000",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_inv.place(x=300,y=300,height=150,width=300)

        self.lbl_inv=Label(self.root,text="Sales\n[0]",bd=5,relief=RIDGE,bg="#F70D1A",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_inv.place(x=650,y=300,height=150,width=300)



        #---footer-----
        lbl_footer=Label(self.root,text="Inventory Management System | Padmavati\n For any Technical Issues contact 9879136395",font=("times new roman",15),bg="#4d636d",fg="white") 
        lbl_footer.pack(side=BOTTOM,fill=X)

#========================================================

    def inventory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=inventoryclass(self.new_win)

    def record(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=recordclass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()