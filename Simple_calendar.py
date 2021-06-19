from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import calendar

root = tk.Tk()
root.geometry('400x400')
root.title('Calender')


def show(): 
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y, m)

    cal.insert('end', output)


def clear():
    cal.delete(1.0, 'end')


def exit():
    root.destroy()

#logo of calendar
img = ImageTk.PhotoImage(Image.open('calendar_logo_f.jpg'))
label = Label(image=img)
label.place(x=62, y=-72)

#for spinbox to choose year month 
m_label = Label(root, text="Month", font=('verdana', '10', 'bold'))
m_label.place(x=70, y=200)

month = Spinbox(root, from_=1, to=12, width="5")
month.place(x=140, y=200)

y_label = Label(root, text="Year", font=('verdana', '10', 'bold'))
y_label.place(x=210, y=200)

year = Spinbox(root, from_=2020, to=3000, width="8")
year.place(x=260, y=200)

#text box to show the calendar
cal = Text(root, width=25, height=8, relief=RIDGE, borderwidth=5)
cal.place(x=100, y=225)

#function calling to show and all
show = Button(root, text="Show", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=show)
show.place(x=120, y=370)

clear = Button(root, text="Clear", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear.place(x=180, y=370)

exit = Button(root, text="Exit", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=exit)
exit.place(x=240, y=370)
root.mainloop()
