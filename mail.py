import smtplib
import turtle
from turtle import*

def send_mail():
    turt = turtle.Turtle()
    screen = Screen()
    screen.setup(width=450, height=500)
    turt.hideturtle()
    turt.penup()
    turt.backward((turt.getscreen().window_width() / 2) - 10)
    message = "Before using this mail application\nmake sure that less secure app access is\nturned on in your google account :)"
    turt.write(message, move=False, font=('monaco', 15, 'bold'), align='left')
    turtle.title("Mail")
    my_email = screen.textinput(title="Mail", prompt="Mail ID")
    my_password = screen.textinput(title="Mail", prompt="Enter your Password")
    my_email2 = screen.textinput(title="Mail", prompt="Send to?")
    subject = screen.textinput(title="Mail", prompt="Subject")
    new_msg = screen.textinput(title="Mail", prompt="Message")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email2, msg=f"Subject:{subject}\n\n{new_msg}")
    setposition(50, -50)
    turtle.write("Sent", font=("Verdana", 24, "bold"))
