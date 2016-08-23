#coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
server = smtplib.SMTP('smtp.163.com', 25)
server.login('Hintat0928@163.com', 'lh19900928')
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = 'Hintat<Hintat0928@163.com>'
msg['Subject'] = Header(u'text', 'utf8').encode()
msg['To'] = 'Hintat<409365364@qq.com>'
server.sendmail('Hintat0928@163.com', ['409365364@qq.com'], msg.as_string())