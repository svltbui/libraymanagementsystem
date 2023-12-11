from  tkinter import* 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
class librayManagement:
    def __init__(self, root):
        self.root=root
        self.root.title("Libray Management System")
        self.root.geometry("1550x800+0+0")
        
        #======================================= variable==============================
        self.member_ver=StringVar()
        self.idno_ver=StringVar()
        self.firstname_ver=StringVar()
        self.lastname_ver=StringVar()
        self.adress1_ver=StringVar()
        self.adress2_ver=StringVar()
        self.postcode_ver=StringVar()
        self.mobile_ver=StringVar()
        self.bookid_ver=StringVar()
        self.booktitle_ver=StringVar()
        self.author_ver=StringVar()
        self.dateborrowed_ver=StringVar()
        self.datedue_ver=StringVar()
        self.dayson_ver=StringVar()
        self.latereternfine_ver=StringVar()
        self.dateoverdate_ver=StringVar()
        self.finalprice=StringVar()
        
        lbltitle=Label(self.root,text="Libray Management System" , bg="powder blue", fg="green", bd="20" , relief=RIDGE , font=("times new roman" ,50,"bold"), padx=2, pady =6 )
        lbltitle.pack(side="top", fill=X)
        
        frame=Frame(self.root, bd=12 , padx=10, relief=RIDGE , bg="powder blue")
        frame.place(x=0 , y= 130 , width="1530" ,height="400")
        #================================== DataFrameLeft =============================
        DataFrameLeft=LabelFrame(frame , text="Libray Member Information " , bg="powder blue", fg="black", bd="12" , relief=RIDGE , font=("times new roman" ,12,"bold"))
        DataFrameLeft.place(x=0,y=5, width="860" , height= "350")
        lblmembership=Label(DataFrameLeft , text="Member type" ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lblmembership.grid(row=0, column=0 ,sticky=W)
        
        comMember= ttk.Combobox(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.member_ver , width= 27 , state="readonly")
        comMember["value"]=("Admin Staff" , "Lecturer", "Student")
        comMember.grid(row=0 , column=1)
        
        lblidno=Label(DataFrameLeft , text="ID NO: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =4 )
        lblidno.grid(row=1, column=0 ,sticky=W)
        txtidno=Entry(DataFrameLeft, font=("times new roman" ,12,"bold") ,textvariable=self.idno_ver, width= 29)
        txtidno.grid(row=1,column=1)
        
        lblfristname=Label(DataFrameLeft ,text="Frist Name: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lblfristname.grid(row=2, column=0 ,sticky=W)
        txtfristname=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.firstname_ver , width= 29)
        txtfristname.grid(row=2,column=1)
        
        lbllastname=Label(DataFrameLeft,text="Last Name: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbllastname.grid(row=3, column=0 ,sticky=W)
        txtlastname=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.lastname_ver , width= 29)
        txtlastname.grid(row=3,column=1)
        
        lbladdress1=Label(DataFrameLeft,text="Address1 : " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbladdress1.grid(row=4, column=0 ,sticky=W)
        txtaddress1=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.adress1_ver , width= 29)
        txtaddress1.grid(row=4,column=1)
        
        lbladdress2=Label(DataFrameLeft,text="Address2 : " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbladdress2.grid(row=5, column=0 ,sticky=W)
        txtaddress2=Entry(DataFrameLeft, font=("times new roman" ,12,"bold") ,textvariable=self.adress2_ver, width= 29)
        txtaddress2.grid(row=5,column=1)
        
        lblposcode=Label(DataFrameLeft, text="Post Code : " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =4 )
        lblposcode.grid(row=6, column=0 ,sticky=W)
        txtposcode=Entry(DataFrameLeft, font=("times new roman" ,12,"bold") ,textvariable=self.postcode_ver, width= 29)
        txtposcode.grid(row=6,column=1)
        
        lblmobile=Label(DataFrameLeft,text="Mobile No: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lblmobile.grid(row=7, column=0 ,sticky=W)
        txtmobile=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.mobile_ver , width= 29)
        txtmobile.grid(row=7,column=1)
        
        lblbookid=Label(DataFrameLeft,text="Book ID: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2 )
        lblbookid.grid(row=0, column=2,sticky=W)
        txtbookid=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.bookid_ver , width= 29)
        txtbookid.grid(row=0,column=3)
        
        lblbooktitle=Label(DataFrameLeft ,text="Book Title: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lblbooktitle.grid(row=1, column=2 ,sticky=W)
        txtbooktitle=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.booktitle_ver , width= 29)
        txtbooktitle.grid(row=1,column=3)
        
        lblauthor=Label(DataFrameLeft,text="Athor Name: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lblauthor.grid(row=2, column=2 ,sticky=W)
        txtauthor=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.author_ver , width= 29)
        txtauthor.grid(row=2,column=3)
        
        lbldateborrowed=Label(DataFrameLeft,text="Date Borrowed: "  ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbldateborrowed.grid(row=3, column=2 ,sticky=W)
        tbldateborrowed=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.dateborrowed_ver , width= 29)
        tbldateborrowed.grid(row=3,column=3)
        
        lbldatedue=Label(DataFrameLeft,text="Date Due: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbldatedue.grid(row=4, column=2 ,sticky=W)
        txtdatedue=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.datedue_ver , width= 29)
        txtdatedue.grid(row=4,column=3)
        
        lbldaysonbook=Label(DataFrameLeft,text="Days on Book: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbldaysonbook.grid(row=5, column=2 ,sticky=W)
        txtdaysonbook=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.dayson_ver , width= 29)
        txtdaysonbook.grid(row=5,column=3)
        
        lbllatereturnfine=Label(DataFrameLeft,text="Late Return Fine: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbllatereturnfine.grid(row=6, column=2 ,sticky=W)
        txtlatereturnfine=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.latereternfine_ver , width= 29)
        txtlatereturnfine.grid(row=6,column=3)
        
        lbldateoverdate=Label(DataFrameLeft,text="Date Over Date: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lbldateoverdate.grid(row=7, column=2 ,sticky=W)
        txtdateoverdate=Entry(DataFrameLeft, font=("times new roman" ,12,"bold") ,textvariable=self.dateoverdate_ver, width= 29)
        txtdateoverdate.grid(row=7,column=3)
        
        lblactualprice=Label(DataFrameLeft,text="Actual Price: " ,bg="powder blue" , font=("times new roman" ,12,"bold"), padx=2, pady =6 )
        lblactualprice.grid(row=8, column=2 ,sticky=W)
        txtactualprice=Entry(DataFrameLeft, font=("times new roman" ,12,"bold"),textvariable=self.finalprice , width= 29)
        txtactualprice.grid(row=8,column=3)
        
        
        
        
        
        #================================== DataFrameRight =============================
        DataFrameRight=LabelFrame(frame , text="Books Details " , bg="powder blue", fg="black", bd="12" , relief=RIDGE , font=("arial" ,12,"bold"))
        DataFrameRight.place(x=870,y=5, width="540", height= "350")
        
        self.textBox=Text(DataFrameRight ,font=("times new roman" ,12,"bold") , width= 32 ,height=16,  padx=2, pady=8 )
        self.textBox.grid(row=0, column=2)
        
        listScrolbar= Scrollbar(DataFrameRight )
        listScrolbar.grid(row=0 , column=1 ,sticky="ns")
        
        listsbooks=["Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2nd Edition) ",
                    "Head-First Python: A Brain-Friendly Guide (2nd Edition)","Learn Python the Hard Way: 3rd Edition",
                    "Python Programming: An Introduction to Computer Science","Discrete Mathematics" 
                    , "Think Python " ,"Python everywahre"]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Think Python "):
                self.bookid_ver.set("456455")
                self.booktitle_ver.set("Python Crash Course: A Hands-On")
                self.author_ver.set("David Smith")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("520 TK")
            elif (x=="Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2nd Edition) "):
                self.bookid_ver.set("HD9587")
                self.booktitle_ver.set("Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2nd Edition) ")
                self.author_ver.set("Henry Blowcher")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("420 TK")
            elif (x=="Head-First Python: A Brain-Friendly Guide (2nd Edition)"):
                self.bookid_ver.set("KJ6455")
                self.booktitle_ver.set("Head-First Python: A Brain-Friendly Guide (2nd Edition)")
                self.author_ver.set("Maxim Gorcky")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("985 TK")
            elif (x=="Learn Python the Hard Way: 3rd Edition"):
                self.bookid_ver.set("HU6455")
                self.booktitle_ver.set("Learn Python the Hard Way: 3rd Edition")
                self.author_ver.set("Steve Smith")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("650 TK")
            elif (x=="Python Programming: An Introduction to Computer Science"):
                self.bookid_ver.set("PO4564")
                self.booktitle_ver.set("Python Programming: An Introduction to Computer Science")
                self.author_ver.set("Steven Smith")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("3200 TK")
            elif (x=="Discrete Mathematics"):
                self.bookid_ver.set("AS4564")
                self.booktitle_ver.set("Discrete Mathematics Course: A Hands-On")
                self.author_ver.set("Deren Sami")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("720 TK")
            elif (x=="Python everywahre"):
                self.bookid_ver.set("WE6455")
                self.booktitle_ver.set("Python everywahre: A Hands-On")
                self.author_ver.set("Glen Maxwell")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_ver.set(d1)
                self.datedue_ver.set(d3)
                self.dayson_ver.set(15)
                self.latereternfine_ver.set("25 TK")
                self.dateoverdate_ver.set(" ")
                self.finalprice.set("820 TK")

               
                
        
        listBox=Listbox(DataFrameRight, font=("times new roman" ,12,"bold") , width=20 , height= 16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0, column=0 , padx= 4)
        listScrolbar.config(command=listBox.yview)
        
        for item in listsbooks:
            listBox.insert(END,item)
        
        
        
        # ========================== buttonsFrame ==================================
        framebutton=Frame(self.root, bd=12 , padx=20, relief=RIDGE , bg="powder blue")
        framebutton.place(x=0 , y= 530 , width="1530" ,height="70")
        btnadddata=Button(framebutton, text="Add Data", font=("arial" ,12,"bold") , width=23 , bg="blue" , fg="white",command=self.add_data)
        btnadddata.grid(row=0 , column= 0)
        
        btnShowData=Button(framebutton, text="Show Data", font=("arial" ,12,"bold") , width=23 , bg="blue" , fg="white",command=self.showData)
        btnShowData.grid(row=0 , column= 1)
        
        btnUpdate=Button(framebutton, text="Update", font=("arial" ,12,"bold") , width=23 , bg="blue" , fg="white",command=self.Update)
        btnUpdate.grid(row=0 , column= 2)
        
        btnDelete=Button(framebutton, text="Delete", font=("arial" ,12,"bold") , width=23 , bg="blue" , fg="white",command=self.delete)
        btnDelete.grid(row=0 , column= 3)
        
        btnReset=Button(framebutton, text="Reset", font=("arial" ,12,"bold") , width=23 , bg="blue" , fg="white",command=self.reset)
        btnReset.grid(row=0 , column= 4)
        
        btnExit=Button(framebutton, text="Exit", font=("arial" ,12,"bold") , width=23 , bg="blue" , fg="white",command=self.iExit)
        btnExit.grid(row=0 , column= 5)
        

         # ========================== informationFrame ==================================
        frameDetails=Frame(self.root, bd=12 , padx=20, relief=RIDGE , bg="powder blue")
        frameDetails.place(x=0 , y= 600 , width="1530" ,height="210")
        
        Table_frame=Frame(frameDetails ,  bd=6 , relief=RIDGE , bg="powder blue")
        Table_frame.place(x=0, y=2 , width=1400 , height=180)
        xcroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        ycroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        
        self.libray_table=ttk.Treeview(Table_frame ,columns=("membertype" , "idno"  , "fristname" , "lastname" ,"address1","address2","postcode","mobile",
                                                             "bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdate","actualprice"),xscrollcommand=xcroll,yscrollcommand=ycroll)
        xcroll.pack(side=BOTTOM,fill=X)
        ycroll.pack(side=RIGHT,fill=Y)
        
        xcroll.config(command=self.libray_table .xview)
        ycroll.config(command=self.libray_table .yview)
        
        
        self.libray_table.heading("membertype" , text="Member Type")
        self.libray_table.heading("idno" , text="ID NO.")
        self.libray_table.heading("fristname" , text="First Name")
        self.libray_table.heading("lastname" , text="Last Name")
        self.libray_table.heading("address1" , text="Address 1")
        self.libray_table.heading("address2" , text="Address 2")
        self.libray_table.heading("postcode" , text="Post Code")
        self.libray_table.heading("mobile" , text="Mobile No.")
        self.libray_table.heading("bookid" , text="Book ID")
        self.libray_table.heading("booktitle" , text="Book Title")
        self.libray_table.heading("author" , text="Author Name")
        self.libray_table.heading("dateborrowed" , text="Date of Borrowed")
        self.libray_table.heading("datedue" , text="Due Date")
        self.libray_table.heading("latereturnfine" , text="Late Fine")
        self.libray_table.heading("dateoverdate" , text="Date Over date")
        self.libray_table.heading("actualprice" , text="Final Price")
        
        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH, expand=1)
        
        

        self.libray_table.column("membertype" , width=100)
        self.libray_table.column("idno" , width=100)
        self.libray_table.column("fristname" ,width=100)
        self.libray_table.column("lastname" ,width=100)
        self.libray_table.column("address1" , width=100)
        self.libray_table.column("address2" ,width=100)
        self.libray_table.column("postcode" ,width=100)
        self.libray_table.column("mobile" , width=100)
        self.libray_table.column("bookid" , width=100)
        self.libray_table.column("booktitle" , width=100)
        self.libray_table.column("author" , width=100)
        self.libray_table.column("dateborrowed", width=100)
        self.libray_table.column("datedue" ,width=100)
        self.libray_table.column("latereturnfine",width=100)
        self.libray_table.column("dateoverdate" ,width=100)
        self.libray_table.column("actualprice" ,width=100)
        self.fetch()
        self.libray_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="asdflkjh",database="libray")
        mycursor=conn.cursor()
        mycursor.execute("insert into libray_ values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
            self.member_ver.get(),
            self.idno_ver.get(),
            self.firstname_ver.get(),
            self.lastname_ver.get(),
            self.adress1_ver.get(),
            self.adress2_ver.get(),
            self.postcode_ver.get(),
            self.mobile_ver.get(),
            self.bookid_ver.get(),
            self.booktitle_ver.get(),
            self.author_ver.get(),
            self.dateborrowed_ver.get(),
            self.datedue_ver.get(),
            self.dayson_ver.get(),
            self.latereternfine_ver.get(),
            self.dateoverdate_ver.get(),
            self.finalprice.get()
            
            
        ))
        conn.commit()
        self.fetch()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")
        

    def Update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="asdflkjh",database="libray")
        mycursor=conn.cursor()
        mycursor.execute("update libray_ set member=%s,fristname=%s,lastname=%s,adrees1=%s,adress2=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,author=%s,dateborrowed=%s,datedue=%s,days=%s,latereternfine=%s,dateoverdate=%s,finalprice=%s where idno=%s",(
            self.member_ver.get(),
           
            self.firstname_ver.get(),
            self.lastname_ver.get(),
            self.adress1_ver.get(),
            self.adress2_ver.get(),
            self.postcode_ver.get(),
            self.mobile_ver.get(),
            self.bookid_ver.get(),
            self.booktitle_ver.get(),
            self.author_ver.get(),
            self.dateborrowed_ver.get(),
            self.datedue_ver.get(),
            self.dayson_ver.get(),
            self.latereternfine_ver.get(),
            self.dateoverdate_ver.get(),
            self.finalprice.get(),
            self.idno_ver.get()
                                                                                         


        ))
        conn.commit()
        self.fetch()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated")

    def fetch(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="asdflkjh",database="libray")
        mycursor=conn.cursor()
        mycursor.execute("select * from libray_")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.libray_table.delete(*self.libray_table.get_children())
            for i in rows:
                self.libray_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.libray_table.focus()
        content=self.libray_table.item(cursor_row)
        row=content["values"]
        
        self.member_ver.set(row[0]),
        self.idno_ver.set(row[1]),
        self.firstname_ver.set(row[2]),
        self.lastname_ver.set(row[3]),
        self.adress1_ver.set(row[4]),
        self.adress2_ver.set(row[5]),
        self.postcode_ver.set(row[6]),
        self.mobile_ver.set(row[7]),
        self.bookid_ver.set(row[8]),
        self.booktitle_ver.set(row[9]),
        self.author_ver.set(row[10]),
        self.dateborrowed_ver.set(row[11]),
        self.datedue_ver.set(row[12]),
        self.dayson_ver.set(row[13]),
        self.latereternfine_ver.set(row[14]),
        self.dateoverdate_ver.set(row[15]),
        self.finalprice.set(row[16])
    
    def showData(self):
        self.textBox.insert(END,"Member Type:\t\t"+self.member_ver.get()+ "\n")
        self.textBox.insert(END,"ID NO:\t\t"+self.idno_ver.get()+ "\n")
        self.textBox.insert(END,"Frist Name:\t\t"+self.firstname_ver.get()+ "\n")
        self.textBox.insert(END,"Last Name:\t\t"+self.lastname_ver.get()+ "\n")
        self.textBox.insert(END,"Address 1:\t\t"+self.adress1_ver.get()+ "\n")
        self.textBox.insert(END,"Address 2:\t\t"+self.adress2_ver.get()+ "\n")
        self.textBox.insert(END,"Post Code:\t\t"+self.postcode_ver.get()+ "\n")
        self.textBox.insert(END,"Mobile No:\t\t"+self.mobile_ver.get()+ "\n")
        self.textBox.insert(END,"Book ID:\t\t"+self.bookid_ver.get()+ "\n")
        self.textBox.insert(END,"Book Title:\t\t"+self.booktitle_ver.get()+ "\n")
        self.textBox.insert(END,"Author:\t\t"+self.author_ver.get()+ "\n")
        self.textBox.insert(END,"Date of Borrowed:\t\t"+self.dateborrowed_ver.get()+ "\n")
        self.textBox.insert(END,"DateDue:\t\t"+self.datedue_ver.get()+ "\n")
        self.textBox.insert(END,"DaysOnBook:\t\t"+self.dayson_ver.get()+ "\n")
        self.textBox.insert(END,"LateReturnFine:\t\t"+self.latereternfine_ver.get()+ "\n")
        self.textBox.insert(END,"Date Over Date:\t\t"+self.dateborrowed_ver.get()+ "\n")
        self.textBox.insert(END,"Final Prices:\t\t"+self.finalprice.get()+ "\n")
    def reset(self):
        self.member_ver.set(""),
        self.idno_ver.set(""),
        self.firstname_ver.set(""),
        self.lastname_ver.set(""),
        self.adress1_ver.set(""),
        self.adress2_ver.set(""),
        self.postcode_ver.set(""),
        self.mobile_ver.set(""),
        self.bookid_ver.set(""),
        self.booktitle_ver.set(""),
        self.author_ver.set(""),
        self.dateborrowed_ver.set(""),
        self.datedue_ver.set(""),
        self.dayson_ver.set(""),
        self.latereternfine_ver.set(""),
        self.dateoverdate_ver.set(""),
        self.finalprice.set("") 
        self.textBox.delete("1.0",END)
        
    def iExit(self):
        iexit= messagebox.askyesno("Library Management System" ,"Do you want exit?")
        if iexit>0:
            self.root.destroy()
            return
            

    def delete(self):
        if self.idno_ver.get()=="":
            messagebox.showerror("Error","First give a ID No")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="asdflkjh",database="libray")
            mycursor=conn.cursor()
            query="delete from libray_ where idno=%s"
            value=(self.idno_ver.get(),)
            mycursor.execute(query,value)
            
        conn.commit()
        self.fetch()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success","Member has been Deleted")
        


if __name__ == "__main__":
    root=Tk()
    obj=librayManagement(root)
    root.mainloop()