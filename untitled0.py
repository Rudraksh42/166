from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Working on Canvas using Functions")
root.geometry ("1000x600")
root.configure(background = "mediumturquoise")

canvas = Canvas(root, width = 990, height = 490, bg = "white", highlightbackground = "lightgray")
canvas.pack()

lbl_color = Label(root, text = "Choose Color: ")
lbl_color.place(relx = 0.6, rely = 0.9, anchor = CENTER)

fillcolour = ["Green", "Yellow", "Red", "Blue"]
dropdown = ttk.Combobox(root, state = "readonly", values = fillcolour, width = 10)
dropdown.place(relx = 0.8, rely = 0.9, anchor = CENTER)

coordinate_values = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

lbl_startx = Label(root, text = "StartX")
lbl_startx.place(relx = 0.1, rely = 0.85, anchor = CENTER)
d1 = ttk.Combobox(root, state = "readonly", values = coordinate_values, width = 10)
d1.place(relx = 0.2, rely = 0.85, anchor = CENTER)

lbl_starty = Label(root, text = "StartY")
lbl_starty.place(relx = 0.3, rely = 0.85, anchor = CENTER)
d2 = ttk.Combobox(root, state = "readonly", values = coordinate_values, width = 10)
d2.place(relx = 0.4, rely = 0.85, anchor = CENTER)

lbl_endx = Label(root, text = "EndX")
lbl_endx.place(relx = 0.5, rely = 0.85, anchor = CENTER)
d3 = ttk.Combobox(root, state = "readonly", values = coordinate_values, width = 10)
d3.place(relx = 0.6, rely = 0.85, anchor = CENTER)

lbl_endy = Label(root, text = "EndY")
lbl_endy.place(relx = 0.7, rely = 0.85, anchor = CENTER)
d4 = ttk.Combobox(root, state = "readonly", values = coordinate_values, width = 10)
d4.place(relx = 0.8, rely = 0.85, anchor = CENTER)

def circle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = "c"
    draw(keypress, oldx, oldy, newx, newy)
    
def rectangle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = "r"
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = "l"
    draw(keypress, oldx, oldy, newx, newy)
    
def draw(keypress, oldx, oldy, newx, newy):
    colour = dropdown.get()
    if(keypress == "c"):
        draw_circle = canvas.create_oval(oldx, oldy, newx, newy, fill = colour)
    if(keypress == "r"):
        draw_rectangle = canvas.create_rectangle(oldx, oldy, newx, newy, fill = colour)
    if(keypress == "l"):
        draw_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = colour)
        
root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)

root.mainloop()l