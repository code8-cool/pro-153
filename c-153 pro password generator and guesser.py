# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:22:01 2024

@author: occup
"""

from tkinter import *
import random
root = Tk()
root.geometry("400x400")
label_pass = Label(root, text = "New password")
label_guess = Label(root)
entry = Entry(root)

password = [[  ["A" ,"B" ,"C" ,"D" , "E", "F", "G", "H", "I", "J", "K"],["0" "1", "2", "3", "4", "5", "6", "7", "8","9", ], ["<", "%", "#" , "@", "+"],["r", "u" ,"i" ,"z", "f"], ["zucf", "difb", "cedf", "ghet", "pciz"]  ]]

def show_new_password(): 
    
    inputed = entry.get() 
    randnum1 = random.randint(0,10)
    up_letter1 =  password[0][0][randnum1]
    
    randnum2 = random.randint(0,10)
    num1 =  password[0][1][randnum2]
    
    randnum3 = random.randint(0,4)
    special_char1 =  password[0][2][randnum3]

    randnum4 = random.randint(0,4)
    lower_letter1 =  password[0][3][randnum4]
    
    randnum5 = random.randint(0,4)
    letters1 =  password[0][4][randnum5]

    label_pass["text"] = "Suggested password is : " + up_letter1 + num1 + special_char1 + lower_letter1 + letters1
    label_guess ["text"] = "Guessd password is : " + inputed 
btn = Button(root, text = "show new password", command = show_new_password)
label_pass.place(relx= 0.5, rely = 0.4, anchor = CENTER)
label_guess.place(relx= 0.5, rely = 0.3, anchor = CENTER)
entry.place(relx= 0.5, rely = 0.2, anchor = CENTER)
btn.place(relx= 0.5, rely = 0.5, anchor = CENTER)


root.mainloop()