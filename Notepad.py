from tkinter import *
from time import ctime
from tkinter.filedialog import *
import webbrowser
root = Tk()
root.geometry('500x700')
name = 'Untitled'
root.title(f'{name} :- Notepad ')
root.wm_iconbitmap('C:\\Users\\resurrrector\\Downloads\\notepad.ico')
Textarea = Text(root, font = 'lucida 14')
scroll = Scrollbar(Textarea)
Textarea.pack(expand = True, fill = BOTH)    #expand is used to take the size of window by textarea
scroll.pack(side = RIGHT, fill = Y)
scroll.config(command = Textarea.yview)
Textarea.config(yscrollcommand = scroll.set)
menubar = Menu(root)
file = None
def myFunc():
    pass

def new():
    global file
    root.title('Untitled :- Notepad ')
    file = None
    Textarea.delete(1.0, END)

def open1():
    global file
    file = askopenfile(defaultextension = '.txt', filetypes=[('All Files','*.*'),('Text Documents', '*.txt')])
    if file == " " :
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        Textarea.delete(1.0, END)
        f = open(file, 'r')
        Textarea.insert(1.0, f.read())
        f.close()
def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file == " ":
            file = None
        else:
            f = open(file, 'w')
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' - Notepad')
            print('file Saved')
    else:
        f = open(file, 'w')
        f.write(Textarea.get(1.0, END))
        f.close()

def cut():
    Textarea.event_generate(("<<Cut>>"))

def copy():
    Textarea.event_generate(("<<Copy>>"))

def paste():
    Textarea.event_generate(("<<Paste>>"))

def About_us():
    root1 = Tk()
    root1.minsize(400,400)
    root1.maxsize(400,400)
    root1.title("About Us ")
    Label(root1,text = 'About Us',fg = 'Blue',font = 'FORTE 24 bold').grid(row = 0, column = 0, ipady = 105)
    Label(root1,text = 'Notepad is tool which is used to keep the notes \n and write something which you want to in it',font = 'Tahoma 14').grid(row =1,column =0)
    Label(root1,text = 'Version :---->>>>               Notepad 1.0').grid(ipady = 20)
    Label(root1,text = 'Developer :---->>>>               Kanhaiya Goyal').grid()
    root1.mainloop()

def help():
    url = 'https://www.google.com/search?q=get+help+with+notepad&rlz=1C1CHBF_enIN834IN834&oq=g&aqs=chrome.1.69i57' \
          'j69i59l3j0l4.4262j0j8&sourceid=chrome&ie=UTF-8'
    webbrowser.open(url)

def serch_with_browser():
    webbrowser.open('https://www.google.com/')

def time_date():
    print(ctime())

#File_menu::

file_menu_bar = Menu(menubar, tearoff = 0)  #tearoff = 0 that means when you minimse the window you will not see menubar in small screen
file_menu_bar.add_command(label = 'New', command = new)
file_menu_bar.add_command(label = 'Open', command = open1)
file_menu_bar.add_command(label = 'Save', command = save)

#Edit_menu

Edit_menu_bar = Menu(menubar, tearoff = 0)
Edit_menu_bar.add_command(label = 'Cut', command = cut)
Edit_menu_bar.add_command(label = 'Copy', command = copy)
Edit_menu_bar.add_command(label = 'Paste', command = paste)
Edit_menu_bar.add_separator()
Edit_menu_bar.add_command(label = 'Time / Date', command = time_date)
Edit_menu_bar.add_command(label = 'Search With Browser', command = serch_with_browser)

#.add_cascade is used to define a menubar

menubar.add_cascade(label='File', menu = file_menu_bar)
menubar.add_cascade(label='Edit',menu = Edit_menu_bar)
menubar.add_command(label='Help', command = help)
menubar.add_command(label='About Us', command = About_us)

#.config is used to like pack or grid the menubar

root.config(menu=menubar)

menubar.add_command(label='Exit', command = quit)
root.bind('<<Ctrl+x>>',cut)
root.bind('<<Ctrl+c>>',copy)
root.bind('<<Ctrl+v>>',paste)
root.bind('<<Ctrl+n>>',new)
root.bind('<<Ctrl+o>>',open1)
root.bind('<<Ctrl+s>>',save)
root.mainloop()

#Note :---->>>> Please keep in mind write label, menu instead of Label and Menu and you can see the code for reference