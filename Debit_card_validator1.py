def design(string, card_name):
    from tkinter import Canvas, Tk

    root = Tk()

    root.geometry('400x300')
    root.minsize(400, 300)
    root.maxsize(400, 300)
    w = Canvas(root, width=400, height=300)
    w.pack()
    w.create_rectangle(10, 20, 380, 270, fill="#3498DB")
    w.create_text(150, 30, text=card_name, fill="white", font="Book 16 normal")
    w.create_text(120, 140, text=string, fill="white", font="Harrington 16 normal underline")
    w.create_text(280, 250, text='Verified Successfully', fill="white", font="Book 16 normal")

    root.mainloop()


no = input('Enter the Card Number : ')
if no.isdecimal():
    li = []
    st = []
    card_no_len = len(no)
    for i in no:
        li.append(int(i))
    last_element = li[-1]
    st=li[0:]
    li.pop()
    for i in range(0, len(li),2):
        temp = str(li[i] * 2)
        while (len(temp) != 1):
            sumt = 0
            for j in temp:
                sumt += int(j)
            temp = str(sumt)
        li[i] = int(temp)
else:
    print('Wrong Input ! ')
first_total = sum(li)
if ((first_total+last_element)%10) == 0:
    string = ''
    DC_carte_Blanche = [300,301,302,303,304,305]
    Master_card = [22,23,24,25,26,27,51,52,53,54,55]
    Discover = [601,622,644,645,646,647,648,649]
    Insta_Payment = [637,638,639]
    Visa_Electron_card = [4026,4175,4508,4844,4913,4917]
    Maestro = [5018, 5038, 5020, 5893, 6304, 6759, 6761, 6762, 6763]
    for i in st:
        string += str(i)
    if len(string) == 13 and string[0] == '4':
        card_name = 'Visa Card'
    if len(string) == 14:
        if string[0:2] == '36':
            card_name = 'Diners Club Carte Blanche Card'
        if int(string[0:3]) in DC_carte_Blanche:
            card_name = 'Diners Club Carte Blanche Card'
    if len(string) == 15 and (string[0:2] == '34' or string[0:2] == '37'):
        card_name = 'American Express Card'
    if len(string) >= 16 and len(string) <= 19:
        if string[0] == '4':
            card_name = 'Visa Card'
            design(string,card_name)
        if string[0:2] == '35':
            card_name = 'JCB Card'
            design(string, card_name)
        if string[0:2] == '65':
            card_name = 'Discover Card'
            design(string, card_name)
        if int(string[0:2]) in Master_card:
            card_name = 'Master Card'
            design(string, card_name)
        if int(string[0:3]) in Discover:
            card_name = 'Discover Card'
            design(string, card_name)
        if int(string[0:3]) in Insta_Payment:
            card_name = 'Insta Payment Card'
            design(string, card_name)
        if int(string[0:3]) == 607:
            card_name = 'Rupay Card'
            design(string, card_name)
        if int(string[0:4]) in Maestro:
            card_name = 'Maestro Card'
            design(string, card_name)
        if int(string[0:4]) in Visa_Electron_card:
            card_name = 'Visa Electron Card'
            design(string, card_name)
    else:
        if string[0:2] == '35':
            card_name = 'JCB Card'
            design(string, card_name)
        if string[0:2] == '65':
            card_name = 'Discover Card'
            design(string, card_name)
        if int(string[0:3]) in Discover:
            card_name = 'Discover Card'
            design(string, card_name)
        if int(string[0:4]) in Maestro:
            card_name = 'Maestro Card'
            design(string, card_name)
else:
    print('Unverified Card Number')

