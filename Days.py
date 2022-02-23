import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter.messagebox import *

gui = tk.Tk()
gui.geometry("600x150")
gui.title("Days by date calculator")
gui.config(bg='grey')

x = dt.date.today()
var1 = tk.StringVar(value=x.strftime("%d"))
var2 = tk.StringVar(value=x.strftime("%B"))
var3 = tk.StringVar(value=x.year)
dagen = ttk.Combobox(gui, textvariable=var1, values=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),state="readonly")
maanden = ttk.Combobox(gui, textvariable=var2,values=("January", "February","March","April","May","June","July","August","September","Oktober","November","December"),state="readonly")
jaren = ttk.Combobox(gui, textvariable=var3,values=("2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030"),state="readonly")
dagen.place(x=50,y=50)
maanden.place(x=200,y=50)
jaren.place(x=350,y=50)

def calc():
    global nummer, textInfo
    dag = int(var1.get())
    maand = str(var2.get())
    jaar = int(var3.get())
    gekozenDag = int(dag)
    gekozenMaand = (maand)
    gekozenJaar = int(jaar)
    maandNummer = int(dt.datetime.strptime(gekozenMaand, "%B").month)
    vandaag = x
    gekozenDatum = dt.date(gekozenJaar, maandNummer, gekozenDag)
    verschil = gekozenDatum - vandaag
    nummer = verschil.days
    if nummer > 0:
        if nummer == 1:
            textInfo = "Dit is " + str(nummer) + " dag in de toekomst"
        else:
            textInfo = "Dit zijn " + str(nummer) + " dagen in de toekmost"
    elif nummer < 0:
        if -nummer == 1:
            textInfo = "Dit was " + str(-nummer) + " dag geleden"
        else:
            textInfo = "Dit was " + str(-nummer) + " dagen geleden"
    else:
        textInfo = "Dit is vandaag"

tekst = tk.Label(
    gui,
    font=('arial',15),
    text='Kies de datum die je wilt berekenen',)
tekst.pack()

confirm = tk.Button(
    gui,
    font=('arial',12),
    bg='green',
    text='Bereken',
    command=lambda:[calc(),showinfo(title="Tijdverschil",message=textInfo)])
confirm.place(x=260,y=100)

gui.mainloop()