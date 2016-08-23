# coding=utf-8
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
# 邮件对象:
msg = MIMEMultipart()
# msg = MIMEText('Hello,send by python...', 'plain', 'utf-8')
msg['From'] = 'Hintat<Hintat0928@163.com>'
msg['Subject'] = Header('来自Hintat的问候', 'utf8').encode()
msg['To'] = 'Hintat<409365364@qq.com>'
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(r'C:\Users\Hintat\Desktop\xbx.jpg', 'rb') as x:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='xbx.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='xbx.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(x.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    msg.attach(mime)

from_addr = 'Hintat0928@163.com'
password = 'lh19900928'
smtp_server = 'smtp.163.com'
to_address = '409365364@qq.com'

server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_address, msg.as_string())
server.quit()
