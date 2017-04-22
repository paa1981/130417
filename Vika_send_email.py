# # -*- coding: utf-8 -*-
# import smtplib
# def mail(subject, message, to):
#     smtp_server = 'smtp.ukr.net'
#     smtp_port = 2525
#     sender = 'ukrinterd@ukr.net'
#     smtp_pasword = 'PSMiPAA16'
#     mail_lib = smtplib.SMTP(smtp_server, smtp_port)
#     mail_lib.login(sender, smtp_pasword)
#     # В случае если функции передан не список с получателями
#     # а обычную строку
#     # if isinstance(to, str):
#     #     to = ','.join(to)
#     msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (sender, to, subject)
#     msg += message
#     mail_lib.sendmail(sender, to, msg)
# # отправляем письмо
# message = "KUKU"
# mail('Yeah!', message, 'paa81@mail.ru')

########################

import smtplib

text = open('text.txt')
with open("email.txt", "r") as Email:
    for i in Email:
        receiver = i
        content = text.read()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('paa1981@gmail.com', 'ek130898EK')
        mail.sendmail('paa1981@gmail.com', receiver, content)
        mail.close()
        print('Message have been sent to: ', i)
text.close()





