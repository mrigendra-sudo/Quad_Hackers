import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
# this is the function called when the button is clicked
def Custom():
    os.system('python testing.py')


# this is the function called when the button is clicked
def Ai():
    os.system('python aimode.py')



root = Tk()

# This is the section of code which creates the main window
root.geometry('368x570')
root.configure(background='#FF7F50')
root.title('Pomodoro Timer')


# This is the section of code which creates the a label
Label(root, text='Let\'s get Productive', bg='#FF7F50', font=('arial', 18, 'normal')).place(x=78, y=113)


# This is the section of code which creates a button
Button(root, text='Set Timer', bg='#8B3E2F', font=('arial', 18, 'normal'), command=Custom).place(x=112, y=267)


# This is the section of code which creates a button
Button(root, text='Personalized Timer', bg='#8B3E2F', font=('arial', 18, 'normal'), command=Ai).place(x=63, y=365)


root.mainloop()