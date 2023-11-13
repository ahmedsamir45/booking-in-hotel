from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB_connect import DBConnect
from ListRequests import ListTicket
from Delete_Update import delete
from Delete_Update import Update2

dbconnect = DBConnect()
root = Tk()
root.title('Ticket reservation')
root.configure(background='#7A753C')
#style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background='#7A753C')
style.configure('TButton',background='#7A753C')
style.configure('TRadiobutton',background='#7A753C')








#full name
ttk.Label(root,text='Full Name:').grid(row=0,column=0,padx=10,pady=0)
EntryFullName = ttk.Entry(root,width=30,font=('Arial',16))
EntryFullName.grid(row=0,column=1,columnspan=2,pady=10)
# gender
ttk.Label(root,text='Gender:').grid(row=1,column=0)
spanGender = StringVar()
ttk.Radiobutton(root,text="Male",variable=spanGender,value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=spanGender,value="Female").grid(row=1,column=2)

#comments
ttk.Label(root,text='Comments:').grid(row=2,column=0)
txtComments = Text(root,width=30,height=15,font=('Arial',16))
txtComments.grid(row = 2 , column=1 , columnspan=2 )

#buttons
buSubmit = ttk.Button(root,text='Submit')
buSubmit.grid(row=3,column=3)
buList = ttk.Button(root,text='List Res.')
buList.grid(row=3,column=2)
buDelete = ttk.Button(root,text= 'Delete' )
buDelete.grid(row=3,column=1)
buUpdate = ttk.Button(root,text= 'Update' )
buUpdate.grid(row=3,column=0)
Exit = ttk.Button(root, text="Exit", command=lambda: root.destroy())
Exit.grid(row=4,columnspan=4)



def BuSaveData():
    print('Full Name: {}'.format(EntryFullName.get()))
    print('Gender: {}'.format(spanGender.get()))
    print('Comments: {}'.format(txtComments.get(1.0, 'end')))
    
    
    msg = dbconnect.Add(EntryFullName.get(),spanGender.get(),txtComments.get(1.0, 'end'))
    messagebox.showinfo("Add Info",msg)
    EntryFullName.delete(0,'end')
    txtComments.delete(1.0,'end')

def BuList():
    # TODo show orders
    # print(' not implemented yet ')
    listrequest=ListTicket()

def Delete():
    deleted = delete()

def Update():
    updated = Update2()

buSubmit.config(command=BuSaveData)
buList.config(command=BuList)
buDelete.config(command=Delete)
buUpdate.config(command=Update)

root.mainloop()