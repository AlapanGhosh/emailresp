import easyimap
import smtplib
import time
import os
login=''
password=''
reply=''
def setdt(u,p,r):
    global login,password,reply
    login=u
    password=p
    reply=r
    print(login,password,reply)
def start():
    os.system('cls')
    print('Starting...')
    while(1):
        global login,password,reply
        imapper = easyimap.connect('imap.gmail.com', login, password)
        unseen=imapper.unseen()
        l=len(unseen)
        for mail in unseen:
            print(mail.from_addr)
            print(mail.to)
            print(mail.cc)
            print(mail.title)
            print(mail.body)
            mai = smtplib.SMTP('smtp.gmail.com',587)
            mai.ehlo()
            mai.starttls()
            mai.login(login,password)
            mai.sendmail(login,mail.from_addr,reply)
            mai.close()
        print(l," mail(s) responded")
        time.sleep(15)

    
