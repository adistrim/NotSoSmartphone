from tkinter import *

def open_contact():
    root = Tk()
    root.geometry('400x400')
    root.config(bg='SlateGray3')
    root.resizable(None, None)
    root.title('DataFlair-AddressBook')

    def add():
        global datas
        datas.append([Name.get(), Number.get(), Email.get(1.0, "end-1c")])
        update_book()

    def view():
        Name.set(datas[int(select.curselection()[0])][0])
        Number.set(datas[int(select.curselection()[0])][1])
        Email.delete(1.0, "end")
        Email.insert(1.0, datas[int(select.curselection()[0])][2])

    def delete():
        del datas[int(select.curselection()[0])]
        update_book()

    def reset():
        Name.set('')
        Number.set('')
        Email.delete(1.0, "end")

    def update_book():
        select.delete(0, END)
        for n, p, a in datas:
            select.insert(END, n)

    def quit_contacts():
        root.destroy()

    Name = StringVar()
    Number = StringVar()

    frame = Frame()
    frame.pack(pady=10)

    frame1 = Frame()
    frame1.pack()

    frame2 = Frame()
    frame2.pack(pady=10)

    Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
    Entry(frame, textvariable=Name, width=50).pack()

    Label(frame1, text='Phone No.', font='arial 12 bold').pack(side=LEFT)
    Entry(frame1, textvariable=Number, width=50).pack()

    Label(frame2, text='Email ID', font='arial 12 bold').pack(side=LEFT)
    Email = Text(frame2, width=37, height=4)
    Email.pack()

    Button(root, text="Add", font="arial 12 bold", command=add).place(x=100, y=270)
    Button(root, text="View", font="arial 12 bold", command=view).place(x=100, y=310)
    Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=100, y=350)
    Button(root, text="Reset", font="arial 12 bold", command=reset).place(x=100, y=390)
    Button(root, text="EXIT", font="arial 12 bold", command=quit_contacts, fg="red").place(x=50, y =430)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=200, y=260)
    root.mainloop()