from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ============== variables=========

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        
        # Resize image to window size

         # Resize image to window size

        img = Image.open(r"C:\Users\Siva\Downloads\register wall paper.png")
        img = img.resize((1550, 700), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # ====================left image==============

        img1 = Image.open(r"C:\Users\Siva\Downloads\coffe.png")
        img1 = img1.resize((450, 450), Image.Resampling.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(img1)

        lbl_bg1=Label(self.root,image=self.bg1,bg="white")
        lbl_bg1.place(x=50,y=80,width=450,height=500)

        # =============== main frame ==================

        
        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=80,width=720,height=500)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        # ================ labels and entries ==============

        # ==========row1=============

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12))
        lname_entry.place(x=370,y=130,width=250)

        # ========row2==========

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12))
        email_entry.place(x=370,y=200,width=250)

        # =============third row==========

        security_q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",12),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your Favourite Colour","Your Favourite Person Name","Your First School")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",12))
        self.txt_security.place(x=370,y=270,width=250)

        # ==========4th row=============

        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",12))
        pswd_entry.place(x=50,y=340,width=250)

        
        cpswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpswd.place(x=370,y=310)

        cpswd_entry=ttk.Entry(frame,textvariable=self.var_cpass,font=("times new roman",12))
        cpswd_entry.place(x=370,y=340,width=250)

        # ========== checkbutton================

        self.var_check=IntVar()

        Check_button=Checkbutton(frame,variable=self.var_check,text="I Agree Terms & Conditions",font=("time new roman",8,"bold"),bg="white",onvalue=1,offvalue=0)
        Check_button.place(x=50,y=390)

        # ============ buttons ==========

        img3=Image.open(r"C:\Users\Siva\Downloads\register now.png")
        img3=img3.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimage3,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=80,y=420,width=150)

        img4=Image.open(r"C:\Users\Siva\Downloads\login.png")
        img4=img4.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage4,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=430,y=420,width=150)

        # ========== function declaration============

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Siva1234@",database="management")
            my_cursor=conn.cursor()
            query=("select*from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityq.get(),
                    self.var_securitya.get(),
                    self.var_pass.get(),
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully")




if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

