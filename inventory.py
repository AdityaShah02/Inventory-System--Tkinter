from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import ttk,messagebox
import sqlite3

class inventoryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+300+130")
        self.root.title("INVENTORY MANAGEMENT SYSTEM | PADMAVATI")
        self.root.config(bg="#FFDFDD")
        self.root.focus_force()

        
        
    
        #---------Variables-------
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_prod_id=StringVar()
        self.var_prod_desc=StringVar()
        self.var_ql=StringVar()
        self.var_qp=StringVar()
        self.var_unit=StringVar()
        self.var_location=StringVar()
        self.var_Supplier=StringVar()
        # self.var_date=StringVar()
        # self.var_date_txt=StringVar()

        

        #========search frame==========
        searchframe=LabelFrame(self.root,text="Search product",font=("goudy old style",15,"bold"),bd=2,relief=RIDGE,bg="#FFDFDD")
        searchframe.place(x=250,y=5,width=600,height=70)

        #=========options========
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("Select Option","Product ID","Location","Supplier"),state='readonly',justify=CENTER,font=("goudy old style",13))
        cmb_search.place(x=10,y=10,width=150)
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,fg="white",font=("goudy old style",15,"bold"),bg="lightgrey")
        txt_search.place(x=170,y=10)
        btn_search=Button(searchframe,command=self.search,text="Search",fg="white",font=("goudy old style",15,"bold"),bg="#4caf50",cursor="hand2")
        btn_search.place(x=400,y=8,width=150,height=30)

        #------Title-------
        lbl_title=Label(self.root,text="Inventory",font=("goudy old style",15),bg="blue",fg="white")
        lbl_title.place(x=50,y=80,width=1000)

        #-----content----
        lbl_id=Label(self.root,text="Product ID",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_id.place(x=10,y=120)  
        txt_id=Entry(self.root,textvariable=self.var_prod_id,font=("goudy old style",15),bg="white")
        txt_id.place(x=150,y=120,width=150)

        lbl_desc=Label(self.root,text="Product Description",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_desc.place(x=320,y=120)        
        txt_desc=Entry(self.root,textvariable=self.var_prod_desc,font=("goudy old style",15),bg="white")
        txt_desc.place(x=500,y=120,width=500)

        lbl_ql=Label(self.root,text="Quantity Loose",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_ql.place(x=10,y=160)  
        txt_ql=Entry(self.root,textvariable=self.var_ql,font=("goudy old style",15),bg="white")
        txt_ql.place(x=150,y=160,width=150)

        lbl_unit=Label(self.root,text="Select Unit",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_unit.place(x=320,y=160)  
        combo_unit=ttk.Combobox(self.root,textvariable=self.var_unit,font=('goudy old style',15),width=10,state='readonly')
        combo_unit['value']=('Kg','Gm')
        combo_unit.place(x=500,y=160,width=150)
        combo_unit.current(0)

        # lbl_date=Label(self.root,text="Date",command=self.date,font=("goudy old style",15,"bold"),bg="#FFDFDD")
        # lbl_date.place(x=700,y=160)  
        # txt_date=Entry(self.root,textvariable=self.var_date,font=('goudy old style',15),width=10)
        # txt_date.place(x=800,y=160,width=150)

      
        lbl_id=Label(self.root,text="Quantity Packet",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_id.place(x=10,y=200)  
        txt_id=Entry(self.root,textvariable=self.var_qp,font=("goudy old style",15),bg="white")
        txt_id.place(x=150,y=200,width=150)

        
        lbl_loc=Label(self.root,text="Loacation",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_loc.place(x=320,y=200)  
        # txt_ql=Entry(self.root,textvariable=self.var_ql,font=("goudy old style",15),bg="white")
        # txt_ql.place(x=130,y=160,width=150)
        combo_loc=ttk.Combobox(self.root,textvariable=self.var_location,font=('goudy old style',15),width=10,state='readonly')
        combo_loc['value']=('Select Location','Anand','Ahmedabad')
        combo_loc.current(0)
        combo_loc.place(x=500,y=200,width=200)

        lbl_desc=Label(self.root,text="Supplier",font=("goudy old style",15,"bold"),bg="#FFDFDD")
        lbl_desc.place(x=10,y=240)        
        txt_desc=Entry(self.root,textvariable=self.var_Supplier,font=("goudy old style",15),bg="white")
        txt_desc.place(x=150,y=240,width=150)

        #-------Button-------
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2")
        btn_add.place(x=500,y=240,width=100,height=28)
        
        btn_reset=Button(self.root,command=self.reset,text="Reset",font=("goudy old style",15),bg="#808080",fg="white",cursor="hand2")
        btn_reset.place(x=610,y=240,width=100,height=28)

        btn_delete=Button(self.root,command=self.delete,text="Delete",font=("goudy old style",15),bg="#A52A2A",fg="white",cursor="hand2")
        btn_delete.place(x=720,y=240,width=100,height=28)

        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#008000",fg="white",cursor="hand2")
        btn_update.place(x=830,y=240,width=100,height=28)


        #========= TABLE (RECORD)==========
        rcd_frame=Frame(self.root,bd=3,relief=RIDGE)
        rcd_frame.place(x=0,y=280,relwidth=1,height=220)

        scrolly=Scrollbar(rcd_frame,orient=VERTICAL)
        scrollx=Scrollbar(rcd_frame,orient=HORIZONTAL)

        self.table=ttk.Treeview(rcd_frame,column=("pid","desc","ql","unit","qp","loc","supp"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)

        self.table.heading("pid",text="Product ID")
        self.table.heading("desc",text="Description")
        self.table.heading("ql",text="Quantity Loose")
        self.table.heading("unit",text="Unit")
        self.table.heading("qp",text="Quantity Packet")
        self.table.heading("loc",text="Location")
        self.table.heading("supp",text="Supplier")

        self.table["show"]="headings"

        self.table.column("pid",width=100)
        self.table.column("desc",width=100)
        self.table.column("ql",width=100)
        self.table.column("qp",width=100)
        self.table.column("unit",width=100)
        self.table.column("loc",width=100)
        self.table.column("supp",width=100)
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease-1>",self.get_data)


        self.show()
        


#=======================================================

    def add(self):
      con=sqlite3.connect(database=r'database.db')
      cur=con.cursor()
      try:
          if self.var_prod_id.get()=="":
            messagebox.showerror("Error","Inventory Id is required",parent=self.root)
          else:
            cur.execute("Select * from inventory where pid=?",(self.var_prod_id.get(),))
            cur.execute("Insert into inventory(pid,desc,ql,unit,qp,loc,supp) values(?,?,?,?,?,?,?)",(
                                              self.var_prod_id.get(),
                                              self.var_prod_desc.get(),
                                              self.var_ql.get(),
                                              self.var_unit.get(),
                                              self.var_qp.get(),
                                              self.var_location.get(),
                                              self.var_Supplier.get(),
            
            ))
            con.commit()
            messagebox.showinfo("Success","Inventory Added successfully ")
            self.show()
            self.reset()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
      con=sqlite3.connect(database=r'database.db')
      cur=con.cursor()
      try:
          cur.execute("select * from inventory")
          rows=cur.fetchall()
          self.table.delete(*self.table.get_children())
          for row in rows:
            self.table.insert('',END,values=row)

      except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
      f=self.table.focus()
      content=(self.table.item(f))
      row=content['values']
      self.var_prod_id.set(row[0])
      self.var_prod_desc.set(row[1])
      self.var_ql.set(row[2])
      self.var_unit.set(row[3])
      self.var_qp.set(row[4])
      self.var_location.set(row[5])
      self.var_Supplier.set(row[6])

    def update(self):
      con=sqlite3.connect(database=r'database.db')
      cur=con.cursor()
      try:
          if self.var_prod_id.get()=="":
            messagebox.showerror("Error","Employee Id is required",parent=self.root)
          else:
            cur.execute("Select * from inventory where pid=?",(self.var_prod_id.get(),))
            cur.execute("Update inventory set desc=?,ql=?,unit=?,qp=?,loc=?,supp=? where pid=?",(
                                              
                                              self.var_prod_desc.get(),
                                              self.var_ql.get(),
                                              self.var_unit.get(),
                                              self.var_qp.get(),
                                              self.var_location.get(),
                                              self.var_Supplier.get(),
                                              self.var_prod_id.get(),
            
            ))
            con.commit()
            messagebox.showinfo("Success","Inventory Updated successfully ")
            self.show()
            con.close()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}")


    def delete(self):
      con=sqlite3.connect(database=r'database.db')
      cur=con.cursor()
      try:
          if self.var_prod_id.get()=="":
            messagebox.showerror("Error","Product Id is required",parent=self.root)
            
          else:
            cur.execute("Select * from inventory where pid=?",(self.var_prod_id.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalid Inventory ID",parent=self.root)
            else:
              op=messagebox.askyesno("Confirm","Do you want to delete",parent=self.root)
              cur.execute("delete from inventory where pid=?",(self.var_prod_id.get(),))
              con.commit()
              if op==True:
                cur.execute("delete from inventory where pid=?",(self.var_prod_id.get(),))
                con.commit()
                messagebox.showinfo("Delete","Inventory Deleted Successfully")
                self.reset()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def reset(self):
      self.var_prod_id.set("")
      self.var_prod_desc.set("")
      self.var_ql.set("")
      self.var_unit.set("Kg")
      self.var_qp.set("")
      self.var_location.set("Select Location")
      self.var_Supplier.set("")
      self.var_searchtxt.set("")
      self.var_searchby.set("Select")
      self.show()

    def search(self):
      con=sqlite3.connect(database=r'database.db')
      cur=con.cursor()
      try:
          if self.var_searchby.get()=="Select":
            messagebox.showerror("Error","Select Search By option",parent=self.root)
          elif self.var_searchtxt.get()=="":
            messagebox.showerror("Error","Search input should be required",parent=self.root)
          else:
            cur.execute("select * from inventory where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=cur.fetchall()
            
            if len(row)!=0:
              self.table.delete(*self.table.get_children())
              for row in rows:
                self.table.insert('',END,values=row)
            else:  
              messagebox .showerror("Error","No Record Found!!!",parent=self.root)
      
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=inventoryclass(root)
    root.mainloop()