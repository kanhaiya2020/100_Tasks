# THis progam provides top 11 random designs of Name:

from tkinter import font
from tkinter import *
import random

root = Tk()

# ADD the Size:
name = input("Enter the Name for Design: ")
size_list = [name, name.upper(),name[0].upper()+name[1:]]

# Font Weight:
font_weight_list = ['bold', 'normal']

# Font Weight:
font_style_list = ['bold', 'normal', 'italic']

# Font Family:
font_family_list = ['Ink Free', 'Pristina', 'Colonna MT', 'Times New Roman', 'Segoe Script', 'Old English Text MT', 'Calibri', 'Chiller', 'Curlz MT', 'Algerian', 'Bahnschrift Condensed', 'Bodoni MT Black', 'Brush Script MT', 'Blackadder ITC', 'Wide Latin', 'Bradley Hand ITC', 'Corbel', 'Sitka Banner', 'MV Boli', 'Goudy Stout', 'Segoe MDL2 Assets', 'OCR A Extended', 'Harrington', 'cursive', 'Gill Sans MT Condensed', 'Vladimir Script', 'Footlight MT Light', 'Edwardian Script ITC,', 'Century Gothic', 'Poor Richard', 'Matura MT Script Capitals', 'Arial', 'Jokerman', 'fantasy', 'monospace', 'Harlow Solid Italic', 'Calibri Light', 'Eras Light ITC', 'Lucida Sans Typewriter', 'Bookman Old Style', 'Stencil', 'Gungsuh', 'Informal Roman', 'Viner Hand ITC', 'Kunstler Script', 'Berlin Sans FB Demi', 'Ravie', 'Bahnschrift SemiBold', 'Broadway', 'Bernard MT Condensed', 'Helvetica', 'Comic Sans MS', 'Forte', 'Castellar', 'Script MT Bold', 'Impact', 'Copperplate Gothic Light', 'Juice ITC', 'Magneto', 'Imprint MT Shadow', 'Monotype Corsiva', 'Gigi']

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

# Label and Packing:
for var in range(11):
    name_type = random.choice(size_list)
    size_for_multiple = random.randint(14, 55)
    weight = random.choice(font_weight_list)
    font_family = random.choice(font_family_list)
    myFont = font.Font(family=font_family, size=size_for_multiple, weight=weight)
    text_color = random_text_color()
    w = Label(root, text = name_type, fg = text_color, font = myFont)
    w.pack()

root.mainloop()
