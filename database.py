import sqlite3
from tkinter import messagebox
from tkinter import *

class Queries:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        # self.cur2 = self.conn.cursor()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Member(Member_Type STRING, PRN_No INTEGER, ID_No INTEGER PRIMARY KEY, First_Name STRING,"
            " Last_Name STRING, Address1 STRING, Address2 STRING, Post_code INTEGER, Mobile INTEGER, Book_ID INTEGER , Book_Title STRING,"
            " Author STRING, Date_Borrowed INTEGER, Date_Due INTEGER, Days_On_Book INTEGER, Late_Return_Fine INTEGER,"
            " Date_Over_Due INTEGER, Actual_price INTEGER)")
        self.conn.commit()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Book(Book_ID INTEGER , Book_Title STRING, Author STRING, Actual_Price INTEGER)")
        self.conn.commit()

    def insert(self, Member_Type, PRN_No, ID_No, First_Name, Last_Name, Address1, Address2, Post_Code, Mobile, Book_ID, Book_Title,
               Author, Date_Borrowed, Date_Due, Days_On_Book, Late_Return_Fine, Date_Over_Due, Actual_Price):

        self.cur.execute("INSERT INTO Member VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (Member_Type, PRN_No, ID_No, First_Name, Last_Name, Address1, Address2, Post_Code, Mobile, Book_ID, Book_Title,
                    Author, Date_Borrowed, Date_Due, Days_On_Book, Late_Return_Fine, Date_Over_Due, Actual_Price))

        self.conn.commit()

    def insert1(self, Book_ID, Book_Title, Author, Actual_Price):

        self.cur.execute("INSERT INTO Book VALUES(?, ?, ?, ?) ",(Book_ID, Book_Title, Author, Actual_Price))

        self.conn.commit()
        messagebox.showinfo("Success", "Member has been inserted successfully")

    def update(self, Member_Type, PRN_No, ID_No, First_Name, Last_Name, Address1, Address2, Post_Code, Mobile, Book_ID, Book_Title,
               Author, Date_Borrowed, Date_Due, Days_On_Book, Late_Return_Fine, Date_Over_Due, Actual_Price):

            self.cur.execute("UPDATE Member SET Member_Type =?, PRN_No =?, ID_No =?, First_Name =?, Last_Name =?, Address1 =?, Address2 =?,"
                             " Post_Code =?, Mobile =?, Book_ID =?, Book_Title =?, Author =?, Date_Borrowed =?, Date_Due =?,"
                             " Days_On_Book =?, Late_Return_Fine =?, Date_Over_Due =?, Actual_Price =? WHERE PRN_No =?",
                              (Member_Type, PRN_No, ID_No, First_Name, Last_Name, Address1, Address2, Post_Code, Mobile, Book_ID, Book_Title,
                               Author, Date_Borrowed, Date_Due, Days_On_Book, Late_Return_Fine, Date_Over_Due, Actual_Price,PRN_No))
            self.conn.commit()

    def update1(self, Book_ID, Book_Title, Author, Actual_Price):
            self.cur.execute("UPDATE Book SET Book_ID =?, Book_Title =?, Author =? , Actual_Price=? WHERE Book_ID = ?", (Book_ID, Book_Title, Author
                                                                                                                         , Actual_Price,Book_ID))

            self.conn.commit()

            messagebox.showinfo("Success", "Member has been Updated")


    def fetch_data(self, *args):
        self.cur.execute("SELECT * FROM Member")
        self.conn.commit()

    def fetch_data1(self, *args):
        self.cur.execute("SELECT * FROM Book")
        self.conn.commit()

    def delete(self, Member_Type, PRN_No, ID_No, First_Name, Last_Name, Address1, Address2, Post_Code, Mobile, Book_ID, Book_Title,
               Author, Date_Borrowed, Date_Due, Days_On_Book, Late_Return_Fine, Date_Over_Due, Actual_Price):

            self.cur.execute("DELETE FROM Member where ID_No =  ?", [(ID_No)])
            self.conn.commit()

    def delete1(self, Book_ID, Book_Title, Author, Actual_Price):
            self.cur.execute("DELETE FROM Book WHERE Book_ID = ?", [(Book_ID)])
            self.conn.commit()
            messagebox.showinfo("Delete", "Member has been deleted")
