import tkinter as tk

gui = tk.Tk()
gui.title('Clicker v5')
gui.geometry('250x200')
gui.config(bg="grey")
clicks = 0
check = ''

def colors():
    if clicks < 0:
        gui.config(bg='red')
    elif clicks > 0:
        gui.config(bg='green')
    else:
        gui.config(bg='grey')

def up(e):
    global clicks,check
    clicks += 1
    counter.config(text=clicks)
    counter.pack()
    check='up'
    gui.after(10,colors)

def down(e):
    global clicks,check
    clicks -= 1
    counter.config(text=clicks)
    counter.pack()
    check='down'
    gui.after(10,colors)

def on_enter(e):
   gui.config(bg='yellow')
def on_leave(e):
   gui.config(bg='grey')
    
def doubleclick(e):
    global check, clicks
    if check == 'up':
        clicks *= 3
    elif check == 'down':
        clicks /=3
    counter.config(text= clicks)

button_up = tk.Button(gui,text='up', font=('arial',20,'bold'),command=up)
button_up.pack()

counter = tk.Label(
    gui,
    text=clicks
)
counter.pack()

button_down = tk.Button(gui,text='down', font=('arial',20,'bold'),command=down)
button_down.place(x=75,y=120)

def clicks_config():
    counter.config(text=clicks)
    gui.after(200, autoclick)
    colors()

var1= tk.IntVar()
def autoclick():
    global clicks,check
    if int(var1.get()) == 1:
        if check == 'up':
            clicks += 1
            clicks_config()
        elif check == 'down':
            clicks -= 1
            clicks_config()

autoclick_button = tk.Checkbutton(
    gui,
    text='Autoclicker',
    variable= var1,
    onvalue=1,
    offvalue=0,
    command= autoclick
)
autoclick_button.pack()


button_up.bind("<Enter>", on_enter)
button_up.bind("<Leave>", on_leave)
button_down.bind("<Enter>", on_enter)
button_down.bind("<Leave>", on_leave)
counter.bind('<Double-Button>', doubleclick)
gui.bind('<Up>',up)
button_up.bind('<Button-1>',up)
gui.bind('<Down>',down)
button_down.bind('<Button-1>',down)
gui.bind('<space>', doubleclick)

gui.mainloop()