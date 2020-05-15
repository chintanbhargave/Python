from tkinter import *
from backend import Database

database = Database()

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        #  to fill the entry with current selection 
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass    

    
def view_data():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)


def search_data():
    list1.delete(0,END)
    for row in database.search(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()):
        list1.insert(END,row)


def add_data():
    database.insert(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
    list1.delete(0,END)
    list1.insert(END,(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()))


def delete_data():
    database.delete(selected_tuple[0])


def update_data():
    database.update(selected_tuple[0], title_val.get(), author_val.get(), year_val.get(), isbn_val.get())



window = Tk()

window.wm_title("Book Store")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_val = StringVar()
e1 = Entry(window,textvariable=title_val)
e1.grid(row=0,column=1)

author_val = StringVar()
e2 = Entry(window, textvariable=author_val)
e2.grid(row=0,column=3)

year_val = StringVar()
e3 = Entry(window, textvariable=year_val)
e3.grid(row=1,column=1)

isbn_val = StringVar()
e4 = Entry(window,textvariable=isbn_val)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=40)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="View all", width=12, command= view_data)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search entry", width=12, command=search_data)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add entry", width=12, command=add_data)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update selected", width=12, command=update_data)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete selected", width=12,command=delete_data)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
