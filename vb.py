import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return Age.get()


# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return Gender.get()


# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return comboOneTwoPunch.get()



root = Tk()

# This is the section of code which creates the main window
root.geometry('886x578')
root.configure(background='#7FFF00')
root.title('Welcome to AI mode')


# This is the section of code which creates the a label
Label(root, text='Enter your age group', bg='#7FFF00', font=('arial', 12, 'normal')).place(x=102, y=63)


# This is the section of code which creates a combo box
Age= ttk.Combobox(root, values=['Age_18-20', 'Age_21-25', 'Age_26-30', 'Age_31-35', 'Age_<18', 'Age_>36'], font=('arial', 12, 'normal'), width=10)
Age.place(x=290, y=62)
Age.current(1)


# This is the section of code which creates the a label
Label(root, text='Enter your Gender', bg='#7FFF00', font=('arial', 12, 'normal')).place(x=116, y=133)


# This is the section of code which creates a combo box
Gender= ttk.Combobox(root, values=['Gender_F', 'Gender_M'], font=('arial', 12, 'normal'), width=10)
Gender.place(x=290, y=131)
Gender.current(1)


# This is the section of code which creates the a label
Label(root, text='Enter your Program details', bg='#7FFF00', font=('arial', 12, 'normal')).place(x=57, y=200)


# This is the section of code which creates a combo box
comboOneTwoPunch= ttk.Combobox(root, values=['Program_FC', 'Program_IYO', 'Program_Language', 'Program_PM'], font=('arial', 12, 'normal'), width=10)
comboOneTwoPunch.place(x=290, y=195)
comboOneTwoPunch.current(1)


# This is the section of code which creates the a label
Label(root, text='Enter Course', bg='#7FFF00', font=('arial', 12, 'normal')).place(x=151, y=263)


root.mainloop()