#!/usr/bin/python
#BomMail

import os
import smtplib
import getpass
import sys
import time
#from colorama 
#import init, Style, Back, Fore

print ("""
 /$$$$$$$                          /$$      /$$           /$$ /$$      
| $$__  $$                        | $$$    /$$$          |__/| $$      
| $$  \ $$  /$$$$$$  /$$$$$$/$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$      
| $$$$$$$  /$$__  $$| $$_  $$_  $$| $$ $$/$$ $$ |____  $$| $$| $$      
| $$__  $$| $$  \ $$| $$ \ $$ \ $$| $$  $$$| $$  /$$$$$$$| $$| $$      
| $$  \ $$| $$  | $$| $$ | $$ | $$| $$\  $ | $$ /$$__  $$| $$| $$      
| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$ \/  | $$|  $$$$$$$| $$| $$$$$$$$
|_______/  \______/ |__/ |__/ |__/|__/     |__/ \_______/|__/|________/
                                                                                
""")
def BomEmail():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

server = input ('MailServer 1.Gmail/2.Yahoo: ')
user = input('Email: ')
passwd = getpass.getpass('Password: ')


to = input('\nTo: ')
#subject = raw_input('Subject: ')
body = input('Message: ')
total = input('Number of send: ')

if server == 'gmail' or '1' or 'Gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo' or '2' or 'Yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print ("Kindly Enter Your Answer in 1 or 2 in Mail Server.")
    sys.exit()

print ("")

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print ("\r[+]E-mails sent: %i") % i
        sys.stdout.flush()
    server.quit()
    print ("\n Done  !!!")
    print ("                                                  BomMail :~ Enjoy :)")
except KeyboardInterrupt:
    print ("[-] Canceled")
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print ("\n[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps")
    sys.exit()
