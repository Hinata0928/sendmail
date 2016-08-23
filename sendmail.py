#coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
server = smtplib.SMTP('smtp.163.com', 25)
server.login('xxxxxx@xxx.com', 'xxxxxx')
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = 'xxx<xxx@xxx.com>'
msg['Subject'] = Header(u'text', 'utf8').encode()
msg['To'] = 'xxx<xxxxxx@xxx.com>'
server.sendmail('xxxxxx@xxx.com', 'xxxxxx@xx.com'], msg.as_string())
