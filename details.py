from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random 
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime



class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x465+230+170")

     # ================title========================

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,anchor="center",justify="center",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1050,height=50)
        
        #===============logo============================
        
        img2=Image.open(r"C:\Users\Siva\Downloads\hotellogo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

         # ================labelframe=============

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",13,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=400,height=300)

         # floor:

        lbl_cust_floor=Label(labelframeleft,text="Floor No:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=27,font=("arial",8,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

          # room number:

        lbl_cust_roomno=Label(labelframeleft,text="Room No:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_roomno.grid(row=1,column=0,sticky=W)

        self.var_rno=StringVar()

        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_rno,width=27,font=("arial",8,"bold"))
        entry_roomno.grid(row=1,column=1,sticky=W)

          # room type:

        lbl_cust_roomtype=Label(labelframeleft,text="Room Type:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_roomtype.grid(row=2,column=0,sticky=W)

        self.var_rtype=StringVar()

        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_rtype,width=27,font=("arial",8,"bold"))
        entry_roomtype.grid(row=2,column=1,sticky=W)

         # =================btns==========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=200,width=370,height=25)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_reset.grid(row=0,column=3,padx=1)

           
        # ==================table frame search=================== 

        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",13,"bold"),padx=2)
        table_frame.place(x=450,y=55,width=500,height=295)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Room_table=ttk.Treeview(table_frame,column=("floor","roomno","roomtype"),
                                                                   xscrollcommand=scroll_x.set,
                                                                   yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_table.xview)
        scroll_y.config(command=self.Room_table.yview)

        self.Room_table.heading("floor",text="Floor_no")
        self.Room_table.heading("roomno",text="Room_no")
        self.Room_table.heading("roomtype",text="Room_type")

   
        self.Room_table["show"]="headings"
        self.Room_table.column("floor",width=100)
        self.Room_table.column("roomno",width=100)
        self.Room_table.column("roomtype",width=100)

        self.Room_table.pack(fill=BOTH,expand=1)
        self.Room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        
    # add data
        
    def add_data(self):
        if self.var_floor.get()=="" or self.var_rtype.get()=="":
            messagebox.showerror("Error","All fields are required...")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                    self.var_floor.get(),
                    self.var_rno.get(),
                    self.var_rtype.get(),
                   
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success"," New room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

    
    # fetch data
     
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_table.delete(*self.Room_table.get_children())
            for i in rows:
                self.Room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

     # get cursor

    def get_cursor(self,event=""):
        cursor_row=self.Room_table.focus()
        content=self.Room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_rno.set(row[1]),
        self.var_rtype.set(row[2]),

                 
    # update:

    
    def update(self):
        try:
            if self.var_floor.get() == "":
                messagebox.showerror("Error", "Please enter mobile number...", parent=self.root)
                return

            conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""
            update details set 
            Floor_no=%s, Room_type=%s
            where Room_no=%s
        """, (
            self.var_floor.get(),
            self.var_rtype.get(),
            self.var_rno.get(),
           
        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated successfully...", parent=self.root)
        except Exception as e:
            messagebox.showerror("Exception", f"Error occurred: {str(e)}", parent=self.root)


     # delete

    
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do u want to delete this room details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
            my_cursor=conn.cursor()
            query="delete from details where Room_no=%s"
            value=(self.var_rno.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    
    # reset:

    
    def reset(self):
        self.var_floor.set(""),
        self.var_rno.set(""),
        self.var_rtype.set(""),
       

if __name__=="__main__":
    root=Tk()
    object=Details(root)
    root.mainloop()