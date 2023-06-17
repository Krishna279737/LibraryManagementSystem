from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import datetime
import tkinter
from database import Queries
database = Queries("Library.db")

class Library_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

#================================================================VARIABLES=================================================

        self.member = StringVar()
        self.prn = StringVar()
        self.id = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.pootcode = StringVar()
        self.mobile = StringVar()
        self.bookid = StringVar()
        self.booktitle = StringVar()
        self.auther = StringVar()
        self.dateborrowed = StringVar()
        self.datedue = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine = StringVar()
        self.dateoverdue = StringVar()
        self.actualprice = StringVar()


        Lbl_title = Label(self.root, text="Library Management System", fg="red", bd=20, relief="ridge", font="times 60 bold", padx=2, pady=6)
        Lbl_title.pack(side="top", fill="x")

        frame = Frame(self.root, bd=12, relief="ridge", padx=20)
        frame.place(x=0, y=130, width=1530, height=400)

        self.photo1 = PhotoImage(file="Library_images/LMS.png")
        lpic1 = Label(Lbl_title, image=self.photo1, height=99, width=240)
        lpic1.place(x=0, y=0)

        self.photo2 = PhotoImage(file="Library_images/LMS2.png")
        lpic2 = Label(Lbl_title, image=self.photo2, height=99, width=230)
        lpic2.place(x=1260, y=0)

        #==================================================LEFT FRAME DATA=====================================

        leftframe = LabelFrame(frame, text="Library Membership Information", fg="green", bd=12, relief="ridge", font=" arial 12 bold", padx=10)
        leftframe.place(x=0, y=5, width=850, height=360)

        lblmember = Label(leftframe, text="Member Type", font="arial 12 bold", padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

        MemberCombobox = ttk.Combobox(leftframe, textvariable=self.member, font="arial 12", width=27, state="readonly")
        MemberCombobox['value'] = ('Student', 'Teacher')
        MemberCombobox.grid(row=0, column=1)
        MemberCombobox.current(0)

        lblPRN = Label(leftframe, text="PRN No", font="arial 12 bold", padx=2, pady=6)
        lblPRN.grid(row=1, column=0, sticky=W)

        Prn_Entry = Entry(leftframe,textvariable=self.prn, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Prn_Entry.grid(row=1, column=1)

        lblID = Label(leftframe, text="ID No", font="arial 12 bold", padx=2, pady=6)
        lblID.grid(row=2, column=0, sticky=W)

        Id_Entry = Entry(leftframe, textvariable=self.id, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Id_Entry.grid(row=2, column=1)

        lblfname = Label(leftframe, text="First Name", font="arial 12 bold", padx=2, pady=6)
        lblfname.grid(row=3, column=0, sticky=W)

        fname_Entry = Entry(leftframe, textvariable=self.fname, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        fname_Entry.grid(row=3, column=1)

        lblLname = Label(leftframe, text="Last Name", font="arial 12 bold", padx=2, pady=6)
        lblLname.grid(row=4, column=0, sticky=W)

        Lname_Entry = Entry(leftframe, textvariable=self.lname, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Lname_Entry.grid(row=4, column=1)

        lblAddress1 = Label(leftframe, text="Address1", font="arial 12 bold", padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)

        Address1_Entry = Entry(leftframe, textvariable=self.address1, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Address1_Entry.grid(row=5, column=1)

        lblAddress2 = Label(leftframe, text="Address2", font="arial 12 bold", padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)

        Address2_Entry = Entry(leftframe, textvariable=self.address2, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Address2_Entry.grid(row=6, column=1)

        lblPcode = Label(leftframe, text="Poot Code", font="arial 12 bold", padx=2, pady=6)
        lblPcode.grid(row=7, column=0, sticky=W)

        Pcode_Entry = Entry(leftframe, textvariable=self.pootcode, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Pcode_Entry.grid(row=7, column=1)

        lblMobile = Label(leftframe, text="Mobile", font="arial 12 bold", padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)

        Mobile_Entry = Entry(leftframe, textvariable=self.mobile, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Mobile_Entry.grid(row=8, column=1)

        lblBid = Label(leftframe, text="Book ID", font="arial 12 bold", padx=2, pady=6)
        lblBid.grid(row=0, column=2, sticky=W)

        Bid_Entry = Entry(leftframe, textvariable=self.bookid, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Bid_Entry.grid(row=0, column=3)

        lblBtitle = Label(leftframe, text="Book Title", font="arial 12 bold", padx=2, pady=6)
        lblBtitle.grid(row=1, column=2, sticky=W)

        Btitle_Entry = Entry(leftframe, textvariable=self.booktitle, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Btitle_Entry.grid(row=1, column=3)

        lblAuthorname = Label(leftframe, text="Author Name", font="arial 12 bold", padx=2, pady=6)
        lblAuthorname.grid(row=2, column=2, sticky=W)

        Authorname_Entry = Entry(leftframe, textvariable=self.auther, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        Authorname_Entry.grid(row=2, column=3)

        lblDateBorrowed = Label(leftframe, text="Date Due Borrowed", font="arial 12 bold", padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)

        DateBorrowed_Entry = Entry(leftframe, textvariable=self.dateborrowed, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        DateBorrowed_Entry.grid(row=3, column=3)

        lblDateDue = Label(leftframe, text="Date Due", font="arial 12 bold", padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)

        DateDue_Entry = Entry(leftframe, textvariable=self.datedue, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        DateDue_Entry.grid(row=4, column=3)

        lblDaysOnBook = Label(leftframe, text="Days On Book", font="arial 12 bold", padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)

        DaysOnBook_Entry = Entry(leftframe, textvariable=self.daysonbook, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        DaysOnBook_Entry.grid(row=5, column=3)

        lblLateReturnFine = Label(leftframe, text="Late Return Fine", font="arial 12 bold", padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)

        LateReturnFine_Entry = Entry(leftframe, textvariable=self.lateratefine, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        LateReturnFine_Entry.grid(row=6, column=3)

        lblDateOverDue = Label(leftframe, text="Date Over Due", font="arial 12 bold", padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)

        DateOverDue_Entry = Entry(leftframe, textvariable=self.dateoverdue, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        DateOverDue_Entry.grid(row=7, column=3)

        lblActualPrice = Label(leftframe, text="Actual Price", font="arial 12 bold", padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)

        ActualPrice_Entry = Entry(leftframe, textvariable=self.actualprice, font="arial 12", width=29, highlightbackground="gray", highlightthickness=1, highlightcolor="Blue")
        ActualPrice_Entry.grid(row=8, column=3)

# ==================================================RIGHT FRAME DATA=====================================

        Rightframe = LabelFrame(frame, text="Book Details", fg="green", bd=12, relief="ridge", font=" times 12 bold")
        Rightframe.place(x=860, y=5, width=605, height=360)

        lstscrollbar = Scrollbar(Rightframe)
        lstscrollbar.grid(row=0, column=2, sticky="ns")

        Books = ['Head Firt Book', 'Learn Python the Hard Way', 'Python Programing', 'Secrete Rahsys', 'Python Cookbook', 'Intro to Machine Learning',
                 'Fluent Python', 'Programing Python', 'The Algorithm', 'The Tecnich Python', 'Machine Techno', 'My Python']

        def selectbook(event):
            value = str(lstbox.get(lstbox.curselection()))
            x = value
            if x == "Head Firt Book":
                self.bookid.set("BKID56897")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1+d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Learn Python the Hard Way":
                self.bookid.set("BKID89675")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Python Programing":
                self.bookid.set("BKID64523")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Secrete Rahsys":
                self.bookid.set("BKID66451")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Python Cookbook":
                self.bookid.set("BKID35648")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Intro to Machine Learning":
                self.bookid.set("BKID88697")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Fluent Python":
                self.bookid.set("BKID15635")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Programing Python":
                self.bookid.set("BKID56421")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "The Algorithm":
                self.bookid.set("BKID25896")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "The Techinical Python":
                self.bookid.set("BKID78954")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "Machine Techno":
                self.bookid.set("BKID56897")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")

            elif x == "My Python":
                self.bookid.set("BKID12547")
                self.booktitle.set("Head First Kotlin")
                self.auther.set("Harold Davis")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set("14")
                self.lateratefine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.actualprice.set("599")



        lstbox = Listbox(Rightframe, font="arial 12 bold", width=25, height=16, yscrollcommand=lstscrollbar.set)
        lstbox.grid(row=0, column=1, padx=4)
        lstbox.bind("<<ListboxSelect>>", selectbook)

        lstscrollbar.configure(command=lstbox.yview)

        self.txt = Text(Rightframe, font="times 12 bold", width=40, height=16, padx=2, pady=6)
        self.txt.grid(row=0, column=3)

        for Book in Books:
            lstbox.insert(END, Book)
#===================================================================BUTTONS================================================

        Btnframe = Frame(self.root, bd=12, relief="ridge", padx=20)
        Btnframe.place(x=0, y=530, width=1530, height=70)

        BtnAddData = Button(Btnframe, command=self.insert_data, text='ADD DATA', font="arial 16 bold", fg="white", bg="red", width=18)
        BtnAddData.grid(row=0, column=0)

        BtnShowData = Button(Btnframe, command=self.show, text='SHOW DATA', font="arial 16 bold", fg="white", bg="red", width=18)
        BtnShowData.grid(row=0, column=1)

        BtnUpadateData = Button(Btnframe, command=self.update, text='UPDATE', font="arial 16 bold", fg="white", bg="red", width=18)
        BtnUpadateData.grid(row=0, column=2)

        BtnDeleteData = Button(Btnframe, command=self.delete_data, text='DELETE', font="arial 16 bold", fg="white", bg="red", width=18)
        BtnDeleteData.grid(row=0, column=3)

        BtnResetData = Button(Btnframe, command=self.reset, text='RESET', font="arial 16 bold", fg="white", bg="red", width=18)
        BtnResetData.grid(row=0, column=4)

        BtnExitData = Button(Btnframe, command=self.Exit, text='EXIT', font="arial 16 bold", fg="white", bg="red", width=18)
        BtnExitData.grid(row=0, column=5)

#===================================================================Information================================================

        framedetails = Frame(self.root, bd=12, relief="ridge", padx=20)
        framedetails.place(x=0, y=600, width=1530, height=200)

        TableFrame = Frame(framedetails, bd=6, relief="ridge")
        TableFrame.place(x=0, y=2, width=1470, height=175)

        treescrollbar1 = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        treescrollbar1.pack(side=BOTTOM, fill="x")
        treescrollbar2 = ttk.Scrollbar(TableFrame, orient=VERTICAL)
        treescrollbar2.pack(side=RIGHT, fill="y")

        self.tree = ttk.Treeview(TableFrame, xscrollcommand=treescrollbar1, yscrollcommand=treescrollbar2)

        self.tree['columns'] = ('membertype', 'prnno', 'id', 'firstname', 'lastname', 'address1', 'address2', 'pootcode', 'mobile', 'bookid', 'booktitle', 'author',
                                'dateborrowed', 'datedue', 'days', 'latereturnfine', 'dateoverdue', 'finalprice')

        treescrollbar1.config(command=self.tree.xview)
        treescrollbar2.config(command=self.tree.yview)

        self.tree.heading('membertype', text='Member Type')
        self.tree.heading('prnno', text='PRN No')
        self.tree.heading('id', text='ID No')
        self.tree.heading('firstname', text='First Name')
        self.tree.heading('lastname', text='Last Name')
        self.tree.heading('address1', text='Address1')
        self.tree.heading('address2', text='Address2')
        self.tree.heading('pootcode', text='Poot Code')
        self.tree.heading('mobile', text='Mobile')
        self.tree.heading('bookid', text='Book ID')
        self.tree.heading('booktitle', text='Book Title')
        self.tree.heading('author', text='Author')
        self.tree.heading('dateborrowed', text='Date Borrowed')
        self.tree.heading('datedue', text='Date Due')
        self.tree.heading('days', text='Days On Book')
        self.tree.heading('latereturnfine', text='Late Return Fine')
        self.tree.heading('dateoverdue', text='Date Over Due')
        self.tree.heading('finalprice', text='Final Price')

        self.tree["show"] = "headings"
        self.tree.pack(fill="both", expand=TRUE)

        self.tree.column('membertype', width=100)
        self.tree.column('prnno', width=100)
        self.tree.column('id', width=100)
        self.tree.column('firstname', width=100)
        self.tree.column('lastname', width=100)
        self.tree.column('address1', width=100)
        self.tree.column('address2', width=100)
        self.tree.column('pootcode', width=100)
        self.tree.column('mobile', width=100)
        self.tree.column('bookid', width=100)
        self.tree.column('booktitle', width=100)
        self.tree.column('author', width=100)
        self.tree.column('dateborrowed', width=100)
        self.tree.column('datedue', width=100)
        self.tree.column('days', width=100)
        self.tree.column('latereturnfine', width=100)
        self.tree.column('dateoverdue', width=100)
        self.tree.column('finalprice', width=100)

        self.select_data()
        self.tree.bind('<ButtonRelease-1>', self.get_cursor)

#====================================================================DATABASE WORK===============================================================
    def insert_data(self):

        if (self.id.get() == "") and (self.prn.get() == ""):
            messagebox.showerror("ERROR", "Please enter your data")

        database.insert(self.member.get(), self.prn.get(), self.id.get(), self.fname.get(),self.lname.get(), self.address1.get(), self.address2.get(),
        self.pootcode.get(), self.mobile.get(), self.bookid.get(),self.booktitle.get(), self.auther.get(), self.dateborrowed.get(),
        self.datedue.get(), self.daysonbook.get(), self.lateratefine.get(), self.dateoverdue.get(), self.actualprice.get())

        database.insert1(self.bookid.get(), self.booktitle.get(), self.auther.get(),self.actualprice.get())
        self.select_data()

    def update(self):

        if self.id.get() == "" or self.member.get() == "":
            messagebox.showerror("Error", "First Select the Member")
        else:
            database.update(self.member.get(), self.prn.get(), self.id.get(), self.fname.get(),self.lname.get(), self.address1.get(),
                            self.address2.get(),self.pootcode.get(), self.mobile.get(), self.bookid.get(),self.booktitle.get(), self.auther.get(),
                            self.dateborrowed.get(), self.datedue.get(), self.daysonbook.get(), self.lateratefine.get(), self.dateoverdue.get(),
                            self.actualprice.get())

            database.update1(self.bookid.get(), self.booktitle.get(), self.auther.get(), self.actualprice.get())
            self.select_data()


    def delete_data(self):

        if self.id.get() == "" or self.member.get() == "":
            messagebox.showerror("Error", "First Select the Member")
        else:
            database.delete(self.member.get(), self.prn.get(), self.id.get(), self.fname.get(),self.lname.get(), self.address1.get(),
                            self.address2.get(),self.pootcode.get(), self.mobile.get(), self.bookid.get(),self.booktitle.get(), self.auther.get(),
                            self.dateborrowed.get(), self.datedue.get(), self.daysonbook.get(), self.lateratefine.get(), self.dateoverdue.get(),
                            self.actualprice.get())

            database.delete1(self.bookid.get(), self.booktitle.get(), self.auther.get(), self.actualprice.get())

            self.select_data()
            # self.reset()


    def select_data(self):

        database.fetch_data(self.member.get(), self.prn.get(), self.id.get(), self.fname.get(),self.lname.get(), self.address1.get(),
                            self.address2.get(),self.pootcode.get(), self.mobile.get(), self.bookid.get(),self.booktitle.get(), self.auther.get(), self.dateborrowed.get(),
                            self.datedue.get(), self.daysonbook.get(), self.lateratefine.get(), self.dateoverdue.get(), self.actualprice.get())
        rows = database.cur.fetchall()

        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for i in rows:
                self.tree.insert("", END, values=i)


    def get_cursor(self, event):

        cursor = self.tree.focus()
        content = self.tree.item(cursor)
        row = content['values']

        self.member.set(row[0]),
        self.prn.set(row[1]),
        self.id.set(row[2]),
        self.fname.set(row[3]),
        self.lname.set(row[4]),
        self.address1.set(row[5]),
        self.address2.set(row[6]),
        self.pootcode.set(row[7]),
        self.mobile.set(row[8]),
        self.bookid.set(row[9]),
        self.booktitle.set(row[10]),
        self.auther.set(row[11]),
        self.dateborrowed.set(row[12]),
        self.datedue.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.actualprice.set(row[17])

        # self.bookid.set(row[9]),
        # self.booktitle.set(row[10]),
        # self.auther.set(row[11]),
        # self.dateborrowed.set(row[12]),
        # self.datedue.set(row[13]),
        # self.daysonbook.set(row[14]),
        # self.lateratefine.set(row[15]),
        # self.dateoverdue.set(row[16]),
        # self.actualprice.set(row[17])

    def show(self):
        self.txt.insert(END, "Member Type:\t\t" + self.member.get()+"\n")
        self.txt.insert(END, "PRN No:\t\t" + self.prn.get() + "\n")
        self.txt.insert(END, "ID No:\t\t" + self.id.get() + "\n")
        self.txt.insert(END, "First Name:\t\t" + self.fname.get() + "\n")
        self.txt.insert(END, "Last Name:\t\t" + self.lname.get() + "\n")
        self.txt.insert(END, "Address 1:\t\t" + self.address1.get() + "\n")
        self.txt.insert(END, "Address 2:\t\t" + self.address2.get() + "\n")
        self.txt.insert(END, "Poot Code:\t\t" + self.pootcode.get() + "\n")
        self.txt.insert(END, "Mobile:\t\t" + self.mobile.get() + "\n")
        self.txt.insert(END, "Book ID:\t\t" + self.bookid.get() + "\n")
        self.txt.insert(END, "Book Title:\t\t" + self.booktitle.get() + "\n")
        self.txt.insert(END, "Auther:\t\t" + self.auther.get() + "\n")
        self.txt.insert(END, "Date Borrowed:\t\t" + self.dateborrowed.get() + "\n")
        self.txt.insert(END, "Date Due:\t\t" + self.datedue.get() + "\n")
        self.txt.insert(END, "Days On Book:\t\t" + self.daysonbook.get() + "\n")
        self.txt.insert(END, "Late Return Fine:\t\t" + self.lateratefine.get() + "\n")
        self.txt.insert(END, "Date Over Due:\t\t" + self.dateoverdue.get() + "\n")
        self.txt.insert(END, "Actual Price:\t\t" + self.actualprice.get() + "\n")

    def reset(self):

        self.member.set(""),
        self.prn.set(""),
        self.id.set(""),
        self.fname.set(""),
        self.lname.set(""),
        self.address1.set(""),
        self.address2.set(""),
        self.pootcode.set(""),
        self.mobile.set(""),
        self.bookid.set(""),
        self.booktitle.set(""),
        self.auther.set(""),
        self.dateborrowed.set(""),
        self.datedue.set(""),
        self.daysonbook.set(""),
        self.lateratefine.set(""),
        self.dateoverdue.set(""),
        self.actualprice.set("")
        self.txt.delete(1.0, END)

    def Exit(self):
        Exit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if Exit > 0:
            self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    obj = Library_Management_System(root)
    root.mainloop()