#                   IMPORTS
import csv
import sys
import smtplib
from email.message import EmailMessage

#                   CONSTANTS
FRMADDR = 'EMAIL@EMAIL.COM'
PWD = 'PASSWORD'

#                   FUNCTIONS
def email(subject,body,TOADDR,CCADDR):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = FRMADDR
    msg['To'] = TOADDR + ', ' + CCADDR
    recepients = []
    recepients.append(TOADDR)
    recepients.append(CCADDR)
    msg.add_header('Content-Type','text/html')
    msg.set_payload(body)

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(FRMADDR,PWD)
        s.sendmail(msg['From'], recepients, msg.as_string())
        #print(msg.as_string())
        s.quit()
    except Exception as e:
        print('failed')
        print(e)
    return

def createBody(Person1,Person2):
    return 'BODY'


if(len(sys.argv) != 2):
    print('Input correct number of arguments')
    exit()

csvFile = sys.argv[1]

with open(csvFile,newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Mentor Name, Mentor Email, Mentee, Mentee Email, Reason
        email("HEADING",createBody(row[0],row[2]),row[1],row[3])
