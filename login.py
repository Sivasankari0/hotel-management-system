from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

from customer import Cust_page
from room import Room_booking
from details import Details
from hotel import HotelManagementSystem


class Login_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Resize image to window size
        img = Image.open("login wall paper.png")
        img = img.resize((1550, 700), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="whitesmoke")
        frame.place(x=460,y=100,width=340,height=450)

        img1=Image.open("login user.png")
        img1=img1.resize((130,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="whitesmoke",borderwidth=0)
        lblimg1.place(x=580,y=100,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="whitesmoke")
        get_str.place(x=100,y=90)

        # labels

        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="brown",bg="whitesmoke")
        username_lbl.place(x=70,y=130)

        self.txtuser=ttk.Entry(frame,font=("times new roman",12,"bold"),)
        self.txtuser.place(x=40,y=165,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="brown",bg="whitesmoke")
        password_lbl.place(x=70,y=200)

        self.password=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.password.place(x=40,y=230,width=270)


        # ======================icon images==================

        img2=Image.open("login user.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="whitesmoke",borderwidth=0)
        lblimg2.place(x=500,y=233,width=25,height=25)

        img3=Image.open("password.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="whitesmoke",borderwidth=0)
        lblimg3.place(x=500,y=300,width=25,height=25)

        # ============== login btn ================

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="sky blue",activeforeground="white",activebackground="sky blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # ============== register btn ==============

        register_lbl = Button(frame, text="New User Register",command=self.register_window,borderwidth=0,font=("times new roman", 13), fg="brown", bg="whitesmoke")
        register_lbl.place(x=20, y=355)

        # ================== forgot password ============

        forget_lbl = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 13,),borderwidth=0, fg="brown", bg="whitesmoke",)
        forget_lbl.place(x=190, y=355)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Siva Sankari" and self.password.get() == "Masa":
            messagebox.showinfo("Success", "Welcome To Hotel Management System")
        else:
            try:
                import mysql.connector
                conn = mysql.connector.connect(
                host="localhost", user="root", password="Siva1234@", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.password.get(),
                    ))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = HotelManagementSystem(self.new_window)
                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")
        # reset password:

    def reset_password(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)

        else:
            import mysql.connector
            conn = mysql.connector.connect(host="localhost", user="root", password="Siva1234@", database="management")
            my_cursor = conn.cursor()
            query=("select*from register where email=%s and securityq=%s and securitya=%s")
            value=(self.txtuser.get(), self.combo_security_q.get(), self.txt_security.get())

            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login with your new password",parent=self.root2)
                self.root2.destroy()

               




        # forget password:

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
              import mysql.connector
              conn = mysql.connector.connect(
              host="localhost", user="root", password="Siva1234@", database="management")
              my_cursor = conn.cursor()

              query=("select*from register where email=%s")
              value=(self.txtuser.get(),)
              my_cursor.execute(query,value)

              row=my_cursor.fetchone()
              #print(row)

              if row==None:
                  messagebox.showerror("Error","Please enter valid user name")
              else:
                  conn.close()
                  self.root2=Toplevel()
                  self.root2.title("Forgot password")
                  self.root2.geometry("350x420+455+130")

                  l=Label(self.root2,text="Forgot Password",font=("times new roman",17,"bold"),fg="red",bg="white")
                  l.place(x=0,y=10,relwidth=1)

                  security_q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                  security_q.place(x=50,y=80)

                  self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",12),state="readonly")
                  self.combo_security_q["values"]=("Select","Your Birth Place","Your Favourite Colour","Your Favourite Person Name","Your First School")
                  self.combo_security_q.place(x=50,y=130,width=250)
                  self.combo_security_q.current(0)

                  security_a=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                  security_a.place(x=50,y=180)

                  self.txt_security=ttk.Entry(self.root2,font=("times new roman",12))
                  self.txt_security.place(x=50,y=230,width=250)

                  new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                  new_password.place(x=50,y=280)

                  self.new_password=ttk.Entry(self.root2,font=("times new roman",12),show="*")
                  self.new_password.place(x=50,y=330,width=250)

                  btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="green")
                  btn.place(x=140,y=370)


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

        img = Image.open("register wall paper.png")
        img = img.resize((1550, 700), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # ====================left image==============

        img1 = Image.open("coffe.png")
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

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",12),show="*")
        pswd_entry.place(x=50,y=340,width=250)

        
        cpswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpswd.place(x=370,y=310)

        cpswd_entry=ttk.Entry(frame,textvariable=self.var_cpass,font=("times new roman",12),show="*")
        cpswd_entry.place(x=370,y=340,width=250)

        # ========== checkbutton================

        self.var_check=IntVar()

        Check_button=Checkbutton(frame,variable=self.var_check,text="I Agree Terms & Conditions",font=("time new roman",8,"bold"),bg="white",onvalue=1,offvalue=0)
        Check_button.place(x=50,y=390)

        # ============ buttons ==========

        img3=Image.open("register now.png")
        img3=img3.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimage3,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=80,y=420,width=150)

        img4=Image.open("login.png")
        img4=img4.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage4,borderwidth=0,command=self.back_to_login,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=430,y=420,width=150)

        # ========== function declaration============
        
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityq.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password and Confirm password must be same", parent=self.root)
            return
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms & conditions", parent=self.root)
            return
        else:
            try:
                import mysql.connector
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Siva1234@", database="management"
                )
                my_cursor = conn.cursor()
                query = ("SELECT * FROM register WHERE email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email.", parent=self.root)
                    conn.close()
                    return
                else:
                    my_cursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)", (
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
                    messagebox.showinfo("Success", "Registered successfully, now you can login.", parent=self.root)
                    self.root.destroy()  # ✅ Only close if successful
            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}", parent=self.root)



    def back_to_login(self):
        self.root.destroy()


            


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x850+0+0")
    
       #  =========================== 1st img ===========================

        img1=Image.open("ouside hotel.png")
        img1=img1.resize((1100,140),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)  
        lblimg.place(x=0,y=0,width=1550,height=140)

        #============================= logo ==============================
        
        img2=Image.open("hotellogo.png")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        # ===================== title =======================

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,anchor="center",justify="center",relief=RIDGE)
        lbl_title.pack(pady=140,fill="x")

        # ===================== main frame ======================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=210,width=1550,height=620)

        # ========================== menu =========================

        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,anchor="center",justify="center",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        # ======================= button ===========================

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="sky blue",fg="red",bd=0,anchor="center",justify="center",relief=RIDGE,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",width=22,command=self.roombook_details,font=("times new roman",14,"bold"),bg="sky blue",fg="red",bd=0,anchor="center",justify="center",relief=RIDGE,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_page,width=22,font=("times new roman",14,"bold"),bg="sky blue",fg="red",bd=0,anchor="center",justify="center",relief=RIDGE,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        cust_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="sky blue",fg="red",bd=0,anchor="center",justify="center",relief=RIDGE,cursor="hand1")
        cust_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="sky blue",fg="red",bd=0,anchor="center",justify="center",relief=RIDGE,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        # ==================== RIGHT SIDE IMAGE ================
        
        img3=Image.open("receptionist hall.png")
        img3=img3.resize((1090,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1100,height=420)

        # ======================== down image =======================

        img4=Image.open("ouside hotel.png")
        img4=img4.resize((230,190),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=100)

          
        img5=Image.open("food.png")
        img5=img5.resize((230,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=320,width=230,height=100)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_page(self.new_window)

    
    def roombook_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_booking(self.new_window)

     
    def details_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)


            



if __name__ == "__main__":
    root=Tk()
    app=Login_page(root)
    root.mainloop()
