
from tkinter import*
from PIL import Image,ImageTk  # pip install pillow
from customer import Cust_page
from room import Room_booking
from details import Details



class HotelManagementSystem:
    def __init__(self,root,login_root=None):
        self.root=root
        self.login_root = login_root 
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
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="sky blue",fg="red",bd=0,anchor="center",justify="center",relief=RIDGE,cursor="hand1")
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

      

    def logout(self):
        self.root.destroy()
        if self.login_root:
            self.login_root.deiconify()  # Show login window again



if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()