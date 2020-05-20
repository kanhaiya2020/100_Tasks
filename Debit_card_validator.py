no = input('Enter the Card Number : ')
no = str(no)
if no.isdecimal():
    li = []
    card_no_len = len(no)
    for i in no:
        li.append(int(i))
    last_element = li[-1]
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
    print('Verified Successfuly ')
else:
    print('Unverified Card Number')

