from tkinter import *
import os
root = Tk()
root.geometry('800x800')
root.title('News Magzine ')
root.minsize(800,800)
root.maxsize(800,800)
file_path = os.getcwd()+'\\files'
image_path = os.getcwd()+'\\project_image'
files = os.listdir(file_path)
image = os.listdir(image_path)
files_list = []
image_list = []
for var in range(0,len(files)):
    print(files[var])
    f=open(f'files\\{files[var]}','r')
    text = f.read()
    files_list.append(text)
    f.close()

print(files_list)
for var in image:
    image_list.append(var)

f1 = Frame(root,width=800, height=800)
Label(f1, text='News Magzine', font='times 24 bold', bg='Blue').pack()
Label(f1, text=f"{files_list[0]}+\n\n").pack(anchor='w', pady='18', side='left')
f1.pack(side='left', anchor='w')

root.mainloop()