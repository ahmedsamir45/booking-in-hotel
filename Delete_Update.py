from tkinter import *
from tkinter import ttk
from DB_connect import DBConnect

dbconnect = DBConnect()


class delete:
    def __init__(self) :
        self._root = Tk()
        self._style = ttk.Style()
        self._style.theme_use('classic')
        self._style.configure('TLabel',background='#7A753C')
        self._style.configure('TButton',background='#7A753C')
        self._style.configure('TRadiobutton',background='#7A753C')


        self._dbconnect=DBConnect()
        self._root
        label = ttk.Label(self._root,text='Id:')
        label.grid(row=0,column=0)

        entry = ttk.Entry(self._root)
        entry.grid(row=0,column=1)
        button = ttk.Button(self._root,text='DELETE')
        button.grid(row=1,columnspan=2 )

        button.config(command=lambda: dbconnect.DeleteRecord(entry.get()))

        # cursor=self._dbconnect.DeleteRecord(entry.get())
        self._root.mainloop()




class Update2:
    def __init__(self) :
        self._root = Tk()
        self.style =ttk.Style()
        self.style.theme_use('classic')
        self.style.configure('TLabel',background='#7A753C')
        self.style.configure('TButton',background='#7A753C')
        self.style.configure('TRadiobutton',background='#7A753C')

        self._dbconnect=DBConnect()
        
        label = ttk.Label(self._root,text='Id:')
        label.grid(row=0,column=0)

        entry = ttk.Entry(self._root)
        entry.grid(row=0,column=1)
    
       
        #comments
        ttk.Label(self._root,text='Comments:').grid(row=2,column=0)
        txtComments = Text(self._root,width=30,height=15,font=('Arial',16))
        txtComments.grid(row = 2 , column=1 , columnspan=2 )

        #buttons
       
        
        button = ttk.Button(self._root,text='Update')
        button.grid(row=3,columnspan=4 )


        Exit = ttk.Button(self._root, text="Exit", command=lambda: self._root.destroy())
        Exit.grid(row=4,columnspan=4)


        button.config(command=lambda: dbconnect.UpdateRecord(entry.get(),txtComments.get(1.0, 'end') ))

        # cursor=self._dbconnect.DeleteRecord(entry.get())
        self._root.mainloop()
