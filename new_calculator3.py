from tkinter import *


class calculator:
    sub = ''
    samel = ''
    li = []

    def __init__(self):
        self.sub = ''
        self.string = ''
        self.result = ''
        self.rel = []

    def press(self, param):
        self.sub += param
        uservalue.set(self.sub)

    def equation(self):
        try:
            total = eval(self.sub)
            uservalue.set(total)
            self.string = self.sub
            self.result += self.string + ' = ' + str(total) + '\n'
            self.sub = ''
        except:
            uservalue.set('Error ')
            self.sub = ''

    def clear(self):
        self.sub = ' '
        uservalue.set(self.sub)

    def History(self):
        kl = Tk()
        kl.title('History ')
        kl.minsize(400, 300)
        kl.maxsize(400, 300)
        def khatma():
            kl.destroy()

        self.rel = self.result.split('\n')
        print(self.rel)
        frame2b = Frame(kl, bg="DodgerBlue", borderwidth=6, relief=SUNKEN, padx=90)
        frame2b.grid(row=0, column=0)
        Label(frame2b, text='History....', bg='white', fg='black', font='COMSCAN 15 bold').grid(sticky=W)
        Button(kl, text="Clear History", bg='blue', fg='white', font='COMSCAN 15 bold', command=khatma).grid()
        l1 = Listbox(frame2b, bg='orange', fg='black', borderwidth=6, relief=SUNKEN)
        for var in range(len(self.rel)):
            l1.insert(var, self.rel[var])
            print(l1)
        l1.grid(ipadx=20, ipady=20)
        kl.mainloop()

p1 = calculator()
root = Tk()
root.title('Calculator ')
root.minsize(400,300)
root.maxsize(400,300)
uservalue = StringVar()
historyvalue = StringVar()
frame1 = Frame(root, bg="white", borderwidth=6, relief=SUNKEN, padx=45)
frame1.grid(row=0, column=0)
frame2 = Frame(root, bg="DodgerBlue", borderwidth=6, relief=SUNKEN, padx=90)
frame2.grid(row=1, column=0)

st = Entry(frame1, textvariable=uservalue, state='readonly', borderwidth=6, relief=SUNKEN)
st.pack(side=LEFT, fill=Y, ipadx=44, ipady=15)

Button(frame2, text='1', width=5, height=3, command=lambda: p1.press('1')).grid(row=0, column=0)
Button(frame2, text='2', width=5, height=3, command=lambda: p1.press('2')).grid(row=0, column=1)
Button(frame2, text='3', width=5, height=3, command=lambda: p1.press('3')).grid(row=0, column=2)
Button(frame2, text='4', width=5, height=3, command=lambda: p1.press('4')).grid(row=1, column=0)
Button(frame2, text='5', width=5, height=3, command=lambda: p1.press('5')).grid(row=1, column=1)
Button(frame2, text='6', width=5, height=3, command=lambda: p1.press('6')).grid(row=1, column=2)
Button(frame2, text='7', width=5, height=3, command=lambda: p1.press('7')).grid(row=2, column=0)
Button(frame2, text='8', width=5, height=3, command=lambda: p1.press('8')).grid(row=2, column=1)
Button(frame2, text='9', width=5, height=3, command=lambda: p1.press('9')).grid(row=2, column=2)
Button(frame2, text='0', width=5, height=3, command=lambda: p1.press('0')).grid(row=3, column=0)
Button(frame2, text='.', width=5, height=3, command=lambda: p1.press('.')).grid(row=3, column=1, sticky=W)
Button(frame2, text='C', width=5, height=3, command=p1.clear).grid(row=3, column=2, sticky=W + E)
Button(frame2, text='/', width=5, height=3, command=lambda: p1.press('/')).grid(row=0, column=3, sticky=W)
Button(frame2, text='*', width=5, height=3, command=lambda: p1.press('*')).grid(row=1, column=3, sticky=W)
Button(frame2, text='+', width=5, height=3, command=lambda: p1.press('+')).grid(row=2, column=3)
Button(frame2, text='-', width=5, height=3, command=lambda: p1.press('-')).grid(row=3, column=3)
Button(frame2, text='(', width=5, height=3, command=lambda: p1.press('(')).grid(row=0, column=4)
Button(frame2, text=')', width=5, height=3, command=lambda: p1.press(')')).grid(row=1, column=4)
Button(frame2, text='=', width=5, height=3, command=p1.equation).grid(row=2, column=4)
Button(frame2, text='H', width=5, height=3, command=p1.History).grid(row=3, column=4)

root.mainloop()
