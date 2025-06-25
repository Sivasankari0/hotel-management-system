
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random 
import mysql.connector
from tkinter import messagebox


class Cust_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x465+230+170")

        # ===============variables=====================
        
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_father=StringVar()
        self.var_gender=StringVar()
        self.var_postal=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()


        # ================title========================

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,anchor="center",justify="center",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1050,height=50)
        
        #===============logo============================
        
        img2=Image.open(r"C:\Users\Siva\Downloads\hotellogo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # ================labelframe=============

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",13,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=390,height=410)

        # ===============labels and entry===========

        # cust ref:

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=43,font=("arial",8,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # cust name:

        lbl_cust_name=Label(labelframeleft,text="Customer Name:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        txtname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=43,font=("arial",8,"bold"))
        txtname.grid(row=1,column=1)
        
        # father name:

        lbl_cust_mname=Label(labelframeleft,text="Father Name:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)

        txt_mname=ttk.Entry(labelframeleft,textvariable=self.var_cust_father,width=43,font=("arial",8,"bold"))
        txt_mname.grid(row=2,column=1)
        
        # gender:

        lbl_cust_gender=Label(labelframeleft,text="Gender:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",8,"bold"),width=40,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        # post code:

        lbl_cust_post_code=Label(labelframeleft,text="Post Code:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_post_code.grid(row=4,column=0,sticky=W)

        txt_gender=ttk.Entry(labelframeleft,textvariable=self.var_postal,width=43,font=("arial",8,"bold"))
        txt_gender.grid(row=4,column=1)
        
        # mobile number:

        lbl_cust_mobile=Label(labelframeleft,text="Mobile Number:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_mobile.grid(row=5,column=0,sticky=W)

        txt_mobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=43,font=("arial",8,"bold"))
        txt_mobile.grid(row=5,column=1)
        
        # email:

        lbl_cust_email=Label(labelframeleft,text="Email:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=6,column=0,sticky=W)

        txt_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=43,font=("arial",8,"bold"))
        txt_email.grid(row=6,column=1)
        
        # nationality:

        lbl_cust_nationality=Label(labelframeleft,text="Nationality:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_nationality.grid(row=7,column=0,sticky=W)
        
        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",8,"bold"),width=40,state="readonly")
        combo_nation["value"]=("Indian","American","British","Other")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)

        
        # id proof type:

        lbl_cust_id=Label(labelframeleft,text="Id Proof Type:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=8,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",8,"bold"),width=40,state="readonly")
        combo_gender["value"]=("Adhar","Driving Licence","Passport")
        combo_gender.current(0)
        combo_gender.grid(row=8,column=1)
        
        # id number:

        lbl_cust_inum=Label(labelframeleft,text="Id Number:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_inum.grid(row=9,column=0,sticky=W)

        txt_idnum=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=43,font=("arial",8,"bold"))
        txt_idnum.grid(row=9,column=1)
        
        # address:

        lbl_cust_add=Label(labelframeleft,text="Address:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_add.grid(row=10,column=0,sticky=W)

        txt_add=ttk.Entry(labelframeleft,textvariable=self.var_address,width=43,font=("arial",8,"bold"))
        txt_add.grid(row=10,column=1)


        # =================btns==========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=350,width=370,height=25)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_reset.grid(row=0,column=3,padx=1)

        # ==================table=================== 

        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System ",font=("times new roman",13,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=1200,height=410)

        lbl_searchby=Label(table_frame,text="Search By:",font=("arial",8,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,ipady=3)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",8,"bold"),width=20,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=1,ipady=3)

        self.txt_search=StringVar()

        
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=25,font=("arial",8,"bold"))
        txt_search.grid(row=0,column=2,padx=1,ipady=3)

        btn_searchby=Button(table_frame,text="Search",command=self.search,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_searchby.grid(row=0,column=3,padx=1)

        btn_showall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_showall.grid(row=0,column=4,padx=1)

        # ================show table data===============

        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=600,height=300)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","father","gender","post","mobile",
                                                                   "email","nationality","id proof","id number","address"),
                                                                   xscrollcommand=scroll_x.set,
                                                                   yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Postcode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("id proof",text="Id Proof")
        self.Cust_Details_Table.heading("id number",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("id proof",width=100)
        self.Cust_Details_Table.column("id number",width=100)
        self.Cust_Details_Table.column("address",width=100)
        

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_cust_father.get()=="":
            messagebox.showerror("Error","All fields are required...")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_cust_father.get(),
                    self.var_gender.get(),
                    self.var_postal.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_idproof.get(),
                    self.var_idnumber.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from customers")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_cust_father.set(row[2])
        self.var_gender.set(row[3])
        self.var_postal.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10]) 

    def update(self):
        try:
            if self.var_mobile.get() == "":
                messagebox.showerror("Error", "Please enter mobile number...", parent=self.root)
                return

            conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""
            update customers set 
            PName=%s, Father=%s, Gender=%s, Postcode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Addrress=%s 
            where Ref=%s
        """, (
            self.var_cust_name.get(),
            self.var_cust_father.get(),
            self.var_gender.get(),
            self.var_postal.get(),
            self.var_mobile.get(),
            self.var_email.get(),
            self.var_nationality.get(),
            self.var_idproof.get(),
            self.var_idnumber.get(),
            self.var_address.get(),
            self.var_ref.get()
        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully...", parent=self.root)
        except Exception as e:
            messagebox.showerror("Exception", f"Error occurred: {str(e)}", parent=self.root)


   

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do u want to delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
            my_cursor=conn.cursor()
            query="delete from customers where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_cust_father.set("")
        #self.var_gender.set("")
        self.var_postal.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("") 

      
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
        my_cursor = conn.cursor()
        search_by = self.search_var.get()
        search_value = self.txt_search.get()

        query = f"SELECT * FROM customers WHERE {search_by} LIKE %s"
        value = ("%" + search_value + "%",)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__=="__main__":
    root=Tk()
    object=Cust_page(root)
    root.mainloop()