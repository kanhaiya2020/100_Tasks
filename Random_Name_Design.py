from tkinter import messagebox
from tkinter import font
from tkinter import *
import random
root = Tk()
# ADD the Size:
name = input("Enter the Name for Design: ")
size_list = [name, name.upper(),name[0].upper()+name[1:]]
name_type = random.choice(size_list)

# Size for name:
size_for_multiple = random.randint(14,55)

# slant:
slant_list = ['italic', 'roman']
slant = random.choice(slant_list)

# Font Weight:
font_weight_list = ['bold', 'normal']
weight = random.choice(font_weight_list)

# Font Family:
font_family_list = ['Algerian', 'Harrington', 'Bookman Old Style', 'Bernard MT Condensed', 'Blackadder ITC', 'Curlz MT', 'Bradley Hand ITC', 'Brush Script MT', 'Castellar', 'Chiller', 'Comic Sans MS', 'Gigi', 'Times New Roman', 'Helvetica', 'Arial', 'monospace', 'cursive', 'fantasy']
font_family = random.choice(font_family_list)
myFont = font.Font(family=font_family, size=size_for_multiple, weight=weight, slant = slant)

# Text Color:
def random_text_color():
    hex_value = '#'
    for var in range(3):
        rgb = random.randint(0, 255)
        x=str(hex(rgb))[2:]
        if(len(x)==2):
            hex_value+=x
        else:
            hex_value+="0"+x
    return hex_value


text_color = random_text_color()

# Label and Packing:
w = Label (root, text = name_type, fg = text_color, font = myFont)
w.pack()

root.mainloop()
