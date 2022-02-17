import tkinter as tk

gui = tk.Tk()
gui.geometry("700x600")
gui.title("Dambord")

frame = tk.Frame(gui)
a = True

for b in range(10):
    a = not a
    for c in range(10):
        if a == False:
            color = "black"
        else: 
            color = "white"
        a = not a
        tile = tk.Label(frame, bg = color, padx = 30, pady = 20)
        tile.grid(row = b, column = c)
frame.pack()

gui.mainloop()