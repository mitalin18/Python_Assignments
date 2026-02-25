'''Mail sending using SMTP'''

import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password,receiver,subject,body):
    
    #Create email object
    msg = EmailMessage()

    #set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    #adding mail body
    msg.set_content(body)

    #Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    #Login using gamil + app password
    smtp.login(sender,app_password)

    #send the mail
    smtp.send_message(msg)

    #Close connection manually
    smtp.close()


def main():

        #using seperate temp mail acc
        sender_email = "nilapwarmitali@gmail.com"

        #App password generated from google account
        app_password= "umysloxqbalwtszi"

        #Second email for testing
        receiver_email = "mitaliunilapwar@gmail.com" 

        subject = "Test mail from python automation"
        body = "Hello, this is the automated email from Mitali! Have a nice day!"

        send_mail(sender_email,app_password,receiver_email,subject,body)
        print("Mail sent successfully!")

if __name__ == "__main__":
     main()





