from game import*
from mail import*
from music_player import*
from notes_ import*
from contacts import*
from tkinter import*

tk = Tk()
tk.geometry("515x360")
tk.title("Home Screen")
bg = PhotoImage(file="wallpapers/Screenshot 2022-01-18 at 21.38.32.png")
app_screen = LabelFrame(font=("calibri", 15, "bold"), bg="white")
app_screen.place(x=0, y=270, width=515, height=90)
rest_screen = LabelFrame(font=("calibri", 15, "bold"), bg="white")
rest_screen.place(x=0,y=0, width=515, height=270)
label1 = Label(rest_screen, image=bg, width=515, height=270)
label1.place(x=0, y=0)
label2 = Label(app_screen, image=bg, width=515, height=90)
label2.place(x=0, y=0)

txt = Label(text="NOT SO SMARTPHONE", font=("calibri", 20, "bold"), fg="white")
txt2 = Label(text="IS ACTUALLY SMART", font=("calibri", 30, "bold"), fg="white")
txt.place(x=150,y=50)
txt2.place(x=110,y=80)

mail_btn = PhotoImage(file="icons/Screenshot 2022-01-18 at 21.29.55.png")
music_btn = PhotoImage(file="icons/download_copy_84x70 (1).png")
notes_btn = PhotoImage(file="icons/images (1)_copy_84x70.png")
contact_btn = PhotoImage(file="icons/490-4900245_contacts-icon-galaxy-s6-png-image-transparent-background_copy_84x70.png")
game_btn = PhotoImage(file="icons/19-191352_game-icon-png-controller-emoji-transparent-png_copy_84x70.png")
power_btn = PhotoImage(file="icons/download (1)_copy_84x70.png")

def quit_program():
    quit()

button1 = Button(app_screen, image=game_btn, command=gaming, width=70, height=56).grid(row=0, column=4, padx=20, pady=13)
button2 = Button(app_screen, image=mail_btn, command=send_mail, width=70, height=56).grid(row=0, column=1, padx=0, pady=13)
button3 = Button(app_screen, image=notes_btn, command=take_notes, width=70, height=56).grid(row=0, column=3, padx=0, pady=13)
button4 = Button(app_screen, image=contact_btn, command=open_contact, width=70, height=56).grid(row=0, column=0, padx=20, pady=13)
button5 = Button(app_screen, image=music_btn, command=play_music, width=70, height=56).grid(row=0, column=2, padx=20, pady=13)
button6 = Button(rest_screen, image=power_btn, command=quit_program, width=50, height=40).grid(row=0, column=0, padx=2, pady=2)

tk.mainloop()