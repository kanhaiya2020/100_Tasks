#This program is used for simply sending the mail to the receiver with or without attachment through Gmail ID

#importing the Yagmail library
import yagmail
import os
# A simple Python program to demonstrate
# getpass.getpass() to read password
import getpass

print("Before using this programe firstly open the browser and login the gmail ID which will used in this programe \n then click this link and allow the less secure apps \n https://myaccount.google.com/lesssecureapps\n\n")
Sender_Gmail_ID = input('Enter the Sender Gmail which is using by this program:--> \n').lower().strip()
Destination_Gmail_ID = input('Enter the Destination Gmail ID:--> \n').lower().strip()
print('Please Enter the Password Here:---> \n')
try:
    Sender_Password = getpass.getpass()
except Exception as error:
    print('PASSWORD ERROR', error)
Subject = input('Enter the Subject for this Mail:----> \n')
message = input('Type Here your message:---> \n')
CHOICE = input("Do you want add attachment in Mail So type YES: \n").lower().strip()
if CHOICE == 'yes':
    file_name = input('Enter the file name with extainson for attachment:---> \n')
    Path = os.getcwd()+'\\files\\'+file_name
    try:
        #initializing the server connection
        yag = yagmail.SMTP(user=Sender_Gmail_ID, password=Sender_Password)
        #sending the email
        yag.send(to=Destination_Gmail_ID, subject=Subject, contents=message, attachments=Path)
        print("Email sent successfully")
    except:
        print("Error, email was not sent")
else:
    try:
        #initializing the server connection
        yag = yagmail.SMTP(user=Sender_Gmail_ID, password=Sender_Password)
        #sending the email
        yag.send(to=Destination_Gmail_ID, subject=Subject, contents=message)
        print("Email sent successfully")
    except:
        print("Error, email was not sent")
