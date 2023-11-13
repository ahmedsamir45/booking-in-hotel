import sqlite3
from tkinter import messagebox


class DBConnect:
    def __init__(self) :
        self._db = sqlite3.connect('Reservation.db')
        self._db.row_factory = sqlite3.Row
        self._db.execute('create table if not exists Ticket(ID integer primary key autoincrement , Name text , Gender text , comment text )')
        self._db.commit()


    def Add(self,Name,Gender,Comment):
        self._db.execute('insert into Ticket(Name,Gender,Comment) values(?,?,?)',(Name,Gender,Comment))
        self._db.commit()
        return "request is submitted"
    
    def ListRequest(self):
        cursor=self._db.execute("Select * from Ticket")
        return cursor
    
    def DeleteRecord(self,ID):
        x = self._db.execute('select * from Ticket where ID={}'.format((ID)))
        y = x.fetchone()
        print(y)
        if y is not None:
            self._db.execute('delete from Ticket Where ID={}'.format((ID)))
            self._db.commit()
            messagebox.showinfo(title='Success', message="Record is deleted")
            return("Record is deleted")
        else :
            messagebox.showinfo(title='Error', message="The order is not exist")
            return('The order is exist')
    def UpdateRecord(self,ID,Comment):
        x = self._db.execute('select * from Ticket where ID={}'.format((ID)))
        y = x.fetchone()
        print(y)
        if y is not None:
            self._db.execute('update Ticket set comment=? where ID=?',(Comment,ID))
            self._db.commit()
            messagebox.showinfo(title='Success', message="ORder is Updated")
            return('Record is Updated')

        else:    

            messagebox.showinfo(title='Error', message="The order is not exist")
            return('The order is exist')