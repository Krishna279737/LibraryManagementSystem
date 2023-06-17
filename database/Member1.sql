--
-- File generated with SQLiteStudio v3.4.3 on Sat Apr 22 15:15:44 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Member
CREATE TABLE IF NOT EXISTS Member(Member_Type STRING, PRN_No INTEGER, ID_No INTEGER PRIMARY KEY, First_Name STRING, Last_Name STRING, Address1 STRING, Address2 STRING, Post_code INTEGER, Mobile INTEGER, Book_ID INTEGER , Book_Title STRING, Author STRING, Date_Borrowed INTEGER, Date_Due INTEGER, Days_On_Book INTEGER, Late_Return_Fine INTEGER, Date_Over_Due INTEGER, Actual_price INTEGER);
INSERT INTO Member (Member_Type, PRN_No, ID_No, First_Name, Last_Name, Address1, Address2, Post_code, Mobile, Book_ID, Book_Title, Author, Date_Borrowed, Date_Due, Days_On_Book, Late_Return_Fine, Date_Over_Due, Actual_price) VALUES ('Student', 855, 89, 'RADHA', 'KUMARI', 'VRINDAVAN', '', 666, 8569874563, 'BKID64523', 'Head First Kotlin', 'Harold Davis', '2023-04-22 15:12:06.447246', '2023-05-06 15:12:06.447246', 14, 'Rs.25', 'NO', 599);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
