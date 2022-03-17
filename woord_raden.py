import tkinter as tk
from tkinter import ttk, StringVar
from tkinter.messagebox import *
import string
import sys
import os

gui = tk.Tk()
gui.geometry('700x250')
gui.title('Raad het woord')
gui.config(bg='grey')
frame = tk.Frame(gui)
textbox = ttk.Entry(gui)

points = 0
entry_check = ''
woord = []
listunusuble = tk.StringVar(value="A")
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

list1 = []
for x in range(7):
    list1.append(StringVar)

spinbox1 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)
spinbox2 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)
spinbox3 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)
spinbox4 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)
spinbox5 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)
spinbox6 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)
spinbox7 = ttk.Spinbox(frame,textvariable=list1[x],values=alphabet_list,wrap=True,width=2,justify='center',state="readonly",font=5)

letter1 = False
letter2 = False
letter3 = False
letter4 = False
letter5 = False
letter6 = False
letter7 = False
letters = [letter1,letter2,letter3,letter4,letter5,letter6,letter7]

#Start het programma opnieuw op
def rerun():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#woord invoer
entry_word = tk.Label(
    gui,
    text='(4 tot 7 letters)',
    font=('arial',10),
    bg='pink'
)
entry_check = tk.Entry(gui)
entry_word.place(relx=.5, rely=.5, anchor="center")
entry_check.place(relx=.5, rely=.4, anchor="center")

#titel
title=tk.Label(
    gui,
    text=('Vul een woord in'),
    font=('arial',20,'bold')
)
title.place(relx=.5, rely=.25, anchor="s")

#Confirm button
confirm = tk.Button(
    gui,
    text=('Confirm'),
    font=("arial",15,'bold'),
    bg='green',
    command=lambda:[checker()])
confirm.place(relx=.5, rely=.8, anchor="s")

#Checkt het aantal letters
def checker():
    global woord, entry_check
    woord = entry_check.get()
    if len(woord)<4 or len(woord)>7:
        checker()
    else:
        entry_word.destroy(),entry_check.destroy(),title.destroy(),confirm.destroy(),generator()

#Spinboxen genarator
def generator():
    global points
    gok_button.place(x='300',y='150')
    title2.pack()
    frame.pack(pady=50)
    if len(woord) == 4:
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
        points += 24
    elif len(woord) == 5:
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
        spinbox5.grid(row=1, column=5)
        points =+ 30
    elif len(woord) == 6:
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
        spinbox5.grid(row=1, column=5)
        spinbox6.grid(row=1, column=6)
        points =+ 36
    elif len(woord) == 7:
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
        spinbox5.grid(row=1, column=5)
        spinbox6.grid(row=1, column=6)
        spinbox7.grid(row=1, column=7)
        points =+ 42

#messagebox game over
def gameover():
    if points <= 0:
        message = askyesno(title='Game Over',message='Je punten zijn op, het spel is beindigd.\nWil je nog een keer spelen?')
        if message:
            rerun()
        else:
            gui.destroy()

#fouten 
def wrongs(fout):
    for x in range(len(woord)):
        if letters[x] == False:
            fout += 1
    return fout 

#raden
def gok():
    global points
    tempspinboxen = [spinbox1.get(),spinbox2.get(),spinbox3.get(),spinbox4.get(),spinbox5.get(),spinbox6.get(),spinbox7.get()]
    for x in range(len(woord)):
        if tempspinboxen[x] == woord[x]:
            letters[x] = True
            print(letters[x])
        elif tempspinboxen[x] != woord[x]:
            points-=2
            print(points)
        print(tempspinboxen[x])
        fouten = wrongs(0)
    if points <= 0:
        gameover()
    else:
        if fouten == 0:
            message = askyesno(title='Geraden',message='Je hebt het woord geraden!\nWil je nog een keer?')
            if message:
                gui.destroy()
                rerun()
            else:
                gui.destroy()
        elif fouten > 0:
            message = showinfo(title='Raad',message='Er zijn er '+str(fouten)+' fout \nJe hebt nog '+str(points)+' punten')

#titel 2e deel
title2 = tk.Label(gui,
    text='Raad het woord',
    font=('arial',20,'bold')
)

#gok button
gok_button = tk.Button(gui,
    text="Doe een gok",
    command=(gok)
)

gui.mainloop()