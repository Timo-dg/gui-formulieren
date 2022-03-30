import tkinter as tk
from tkinter import ttk
import sys
import os

gui = tk.Tk()
gui.geometry('750x1000')
gui.title('Registratie Formulier')
gui.config(bg='#ffe291')
frame = tk.Frame(gui)
textbox = ttk.Entry(gui)
frame.place(x=300,y=75)

#Restart
def rerun():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Title
title = tk.Label(gui,
text='Registratie Formulier',
font=('arial',20,'bold')
)
title.place(x=230,y=10)

#Voornaam
voornaam_entry = tk.Entry(frame)
voornaam_entry.insert(0, 'Voornaam')
voornaam_entry.grid(row=0,column=1,padx = 5, pady = 5)

#Achternaam
achternaam_entry = tk.Entry(frame)
achternaam_entry.insert(0, 'Achternaam')
achternaam_entry.grid(row=1,column=1,padx = 5, pady = 5)

#Leeftijd
leeftijd_entry = tk.Entry(frame)
leeftijd_entry.insert(0, 'Leeftijd in getal')
leeftijd_entry.grid(row=4,column=1,padx = 5, pady = 5)

#email
email_entry = tk.Entry(frame)
email_entry.insert(0, 'naam@email.com')
email_entry.grid(row=5,column=1,padx = 5, pady = 5)

#Confirm button
confirm_button = tk.Button(frame,
text='Confirm',
command=lambda:[check()]
)
confirm_button.grid(row=7,column=1)

#Check functie
def check():
    email = email_entry.get()
    voornaam = voornaam_entry.get()
    achternaam = achternaam_entry.get()
    leeftijd = leeftijd_entry.get()
    if voornaam == 'Voornaam' or voornaam == '' or achternaam == 'Achternaam' or achternaam == '' or leeftijd == '' or leeftijd == 'Leeftijd in getal':
        print('*Vul alle velden goed in')
        confirm_button.config(bg='red')
    elif leeftijd < str(18):
        print('*Je moet minimaal 18 jaar oud zijn')
    else:
        confirm_button.config(bg='green')        
        print('Ingevulde gegevens: '+voornaam,achternaam,leeftijd,email)
        gegevens(voornaam,achternaam,leeftijd,email)

#Gegevens
def gegevens(voornaam,achternaam,leeftijd,email):
    gegevens_label = tk.Label(gui,
    text=('naam: '+ voornaam+"\n"+ 'Achternaam: ' + achternaam + '\n' + 'Leeftijd: ' + leeftijd + '\n' + 'Email: ' + email ),
    font=('arial',10,'bold')
    )
    frame.destroy()
    gegevens_label.place(x=300,y=250)
    gegevens_buttons()

def gegevens_buttons():
    gegevens_button_versturen = tk.Button(gui,
    text='Versturen',
    command=lambda:[gui.destroy()]
    )
    gegevens_button_versturen.place(x=300,y=350)
    
    gegevens_button_opnieuw = tk.Button(gui,
    text='Vul opnieuw in',
    command=lambda:[rerun()]
    )
    gegevens_button_opnieuw.place(x=400,y=350)


gui.mainloop()