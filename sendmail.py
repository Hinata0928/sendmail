#coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
server = smtplib.SMTP('smtp.163.com', 25)
server.login('xxx@163.com', 'xxx')
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = 'Hintat<xxx@163.com>'
msg['Subject'] = Header(u'text', 'utf8').encode()
msg['To'] = 'Hintat<xxx@qq.com>'
server.sendmail('xxx@163.com', ['xxx@qq.com'], msg.as_string())