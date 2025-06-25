from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random 
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime



class Room_booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x465+230+170")

        # ================variables=====================

        self.var_contact=StringVar()     
        self.var_checkin=StringVar()     
        self.var_checkout=StringVar()    
        self.var_roomtype=StringVar()
        self.var_roomavailability=StringVar()
        self.var_meal=StringVar() 
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar() 
        self.var_total=StringVar()
        


        
        # ================title========================

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,anchor="center",justify="center",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1050,height=50)
        
        #===============logo============================
        
        img2=Image.open("hotellogo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

         # ================labelframe=============

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman",13,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=390,height=410)

        
        # ===============labels and entry===========

        # cust contact:

        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",8,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=27,font=("arial",8,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        # fetch data:

        btn_fetch=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="sky blue",fg="red",width=10)
        btn_fetch.place(x=293,y=4)

        # checkin date:

        check_in_date=Label(labelframeleft,text="Check_in date:",font=("arial",8,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        entry_check_in=ttk.Entry(labelframeleft,width=43,textvariable=self.var_checkin,font=("arial",8,"bold"))
        entry_check_in.grid(row=1,column=1)

        
        # checkout date:

        check_out_date=Label(labelframeleft,text="Check_out date:",font=("arial",8,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        entry_check_out=ttk.Entry(labelframeleft,width=43,textvariable=self.var_checkout,font=("arial",8,"bold"))
        entry_check_out.grid(row=2,column=1)

        
        # room type:

        room_type=Label(labelframeleft,text="Room type:",font=("arial",8,"bold"),padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
        my_cursor=conn.cursor()
       
        
        my_cursor.execute("SELECT DISTINCT Room_type FROM details")
        room_types = my_cursor.fetchall()
        self.combo_room_type = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial",8,"bold"), width=40, state="readonly")
        self.combo_room_type["values"] = [r[0] for r in room_types]
        self.combo_room_type.grid(row=3, column=1)
        self.combo_room_type.bind("<<ComboboxSelected>>", self.update_room_list_on_select)
        
        self.combo_room_type.set("single")
        

        # availability room:

        availability_room=Label(labelframeleft,text="Available room:",font=("arial",8,"bold"),padx=2,pady=6)
        availability_room.grid(row=4,column=0,sticky=W)

        #entry_avail_room=ttk.Entry(labelframeleft,textvariable=self.var_roomavailability,width=43,font=("arial",8,"bold"))
        #entry_avail_room.grid(row=4,column=1)

        self.combo_room_no = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailability, font=("arial",8,"bold"), width=40, state="readonly")
        self.combo_room_no.grid(row=4, column=1)

        # meal:

        meal=Label(labelframeleft,text="Meal:",font=("arial",8,"bold"),padx=2,pady=6)
        meal.grid(row=5,column=0,sticky=W)

        entry_meal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=43,font=("arial",8,"bold"))
        entry_meal.grid(row=5,column=1)

        # no of days:

        no_of_days=Label(labelframeleft,text="No of days:",font=("arial",8,"bold"),padx=2,pady=6)
        no_of_days.grid(row=6,column=0,sticky=W)

        entry_no_of_days=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=43,font=("arial",8,"bold"))
        entry_no_of_days.grid(row=6,column=1)

        # paid tax:

        paid_tax=Label(labelframeleft,text="Paid tax:",font=("arial",8,"bold"),padx=2,pady=6)
        paid_tax.grid(row=7,column=0,sticky=W)

        entry_paid_tax=ttk.Entry(labelframeleft,width=43,textvariable=self.var_paidtax,font=("arial",8,"bold"))
        entry_paid_tax.grid(row=7,column=1)

        # sub total:

        sub_total=Label(labelframeleft,text="Sub total:",font=("arial",8,"bold"),padx=2,pady=6)
        sub_total.grid(row=8,column=0,sticky=W)

        entry_sub_total=ttk.Entry(labelframeleft,width=43,textvariable=self.var_actualtotal,font=("arial",8,"bold"))
        entry_sub_total.grid(row=8,column=1)

        
        # total cost:

        total_cost=Label(labelframeleft,text="Total cost:",font=("arial",8,"bold"),padx=2,pady=6)
        total_cost.grid(row=9,column=0,sticky=W)

        entry_total_cost=ttk.Entry(labelframeleft,width=43,textvariable=self.var_total,font=("arial",8,"bold"))
        entry_total_cost.grid(row=9,column=1)

        #==================bill button===================

        btn_bill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",8,"bold"),bg="sky blue",fg="red",width=8)
        btn_bill.grid(row=10,column=0,padx=7,sticky=W)


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

        
        # ==================table frame search=================== 

        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System ",font=("times new roman",13,"bold"),padx=2)
        table_frame.place(x=400,y=250,width=1200,height=210)

        lbl_searchby=Label(table_frame,text="Search By:",font=("arial",8,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,ipady=3)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",8,"bold"),width=20,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=1,ipady=3)

        self.txt_search=StringVar()

        
        txt_search=ttk.Entry(table_frame,width=25,textvariable=self.txt_search,font=("arial",8,"bold"))
        txt_search.grid(row=0,column=2,padx=1,ipady=3)

        btn_searchby=Button(table_frame,text="Search",command=self.search,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_searchby.grid(row=0,column=3,padx=1)

        btn_showall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",8,"bold"),bg="sky blue",fg="red",width=12)
        btn_showall.grid(row=0,column=4,padx=1)

        # =================room image==================

        
        img3=Image.open("room.png")
        img3=img3.resize((300,190),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=730,y=55,width=300,height=190)

         # ================show table data===============

        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=635,height=130)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailability","meal",
                                                                   "noofdays"),
                                                                   xscrollcommand=scroll_x.set,
                                                                   yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_table.xview)
        scroll_y.config(command=self.Room_table.yview)

        self.Room_table.heading("contact",text="Mobile")
        self.Room_table.heading("checkin",text="Check-In")
        self.Room_table.heading("checkout",text="Check-Out")
        self.Room_table.heading("roomtype",text="Room Type")
        self.Room_table.heading("roomavailability",text="Room No")
        self.Room_table.heading("meal",text="Meal")
        self.Room_table.heading("noofdays",text="No Of Days")
   

        self.Room_table["show"]="headings"
        self.Room_table.column("contact",width=100)
        self.Room_table.column("checkin",width=100)
        self.Room_table.column("checkout",width=100)
        self.Room_table.column("roomtype",width=100)
        self.Room_table.column("roomavailability",width=100)
        self.Room_table.column("meal",width=100)
        self.Room_table.column("noofdays",width=100)

        self.Room_table.pack(fill=BOTH,expand=1)
        self.Room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # add data
        
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required...")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailability.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                 
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

    # fetch data
     
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_table.delete(*self.Room_table.get_children())
            for i in rows:
                self.Room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
      
    
    def get_cursor(self,event=""):
        cursor_row=self.Room_table.focus()
        content=self.Room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailability.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6]),
                 
    # update:

    
   
    def update(self):
        try:
            if self.var_contact.get() == "":
                messagebox.showerror("Error", "Please enter mobile number...", parent=self.root)
                return

            conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""
            update room set 
            Check_in=%s, Check_out=%s, Room_type=%s, Room=%s, Meal=%s, No_of_days=%s
            where Contact=%s
        """, (
            self.var_checkin.get(),
            self.var_checkout.get(),
            self.var_roomtype.get(),
            self.var_roomavailability.get(),
            self.var_meal.get(),
            self.var_noofdays.get(),
            self.var_contact.get(),
           
        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully...", parent=self.root)
        except Exception as e:
            messagebox.showerror("Exception", f"Error occurred: {str(e)}", parent=self.root)


    # delete

    
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do u want to delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Siva1234@",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    # reset:

    
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        #self.var_roomtype.set(""),
        self.var_roomavailability.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set(""),
    
    def update_room_list_on_select(self, event):
        selected_type = self.var_roomtype.get()
        conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Room_no FROM details WHERE Room_type = %s", (selected_type,))
        room_numbers = my_cursor.fetchall()
        conn.close()

        self.combo_room_no["values"] = [r[0] for r in room_numbers]
        if room_numbers:
            self.combo_room_no.current(0)
        else:
            self.combo_room_no.set("")

       

        #==============================all data fetch======================

    
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
            my_cursor = conn.cursor()
            query=("select PName from customers where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=410,y=60,width=300,height=185)

            

                lblName=Label(showDataFrame,text="Name:",font=("arial",8,"bold"))
                lblName.place(x=0,y=0)

                lbl1=Label(showDataFrame,text=row[0],font=("arial",8,"bold"))
                lbl1.place(x=90,y=0)

               # ==============gender============

                conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
                my_cursor = conn.cursor()
                query=("select Gender from customers where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataFrame,text="Gender:",font=("arial",8,"bold"))
                lblgender.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("arial",8,"bold"))
                lbl2.place(x=90,y=30)

                # ==============email============

                conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
                my_cursor = conn.cursor()
                query=("select Email from customers where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataFrame,text="Email:",font=("arial",8,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataFrame,text=row,font=("arial",8,"bold"))
                lbl3.place(x=90,y=60)

                # ==============nationality============

                conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
                my_cursor = conn.cursor()
                query=("select Nationality from customers where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnation=Label(showDataFrame,text="Nationality:",font=("arial",8,"bold"))
                lblnation.place(x=0,y=90)

                lbl4=Label(showDataFrame,text=row,font=("arial",8,"bold"))
                lbl4.place(x=90,y=90)

                # ==============address============

                conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
                my_cursor = conn.cursor()
                query=("select Addrress from customers where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdr=Label(showDataFrame,text="Addrress:",font=("arial",8,"bold"))
                lbladdr.place(x=0,y=120)

                lbl5=Label(showDataFrame,text=row,font=("arial",8,"bold"))
                lbl5.place(x=90,y=120)

    # search system:

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Siva1234@", database="management")
        my_cursor = conn.cursor()
        search_by = self.search_var.get()
        search_value = self.txt_search.get()

        query = f"SELECT * FROM room WHERE {search_by} LIKE %s"
        value = ("%" + search_value + "%",)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_table.delete(*self.Room_table.get_children())
            for i in rows:
                self.Room_table.insert("", END, values=i)
            conn.commit()
        conn.close()




    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")

        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="single"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="double"):
            q1=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="single"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="double"):
            q1=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="single"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="double"):
            q1=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Full time" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif(self.var_meal.get()=="Full time" and self.var_roomtype.get()=="double"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif(self.var_meal.get()=="Full time" and self.var_roomtype.get()=="luxury"):
            q1=float(700)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
    


if __name__=="__main__":
    root=Tk()
    object=Room_booking(root)
    root.mainloop()