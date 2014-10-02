import smtplib, email
#from and import key word make it possible that use a variable stand for a specified module name
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
#from key word copy a module variable name to a specified domain
from email.utils import parseaddr, formataddr

#def a function to format email address
def _format_addr(s):
    (name, addr) = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr))

#get address and other by input
#from_addr = input('From: ')
#from_name = input('MyName: ')
#password = input('Password: ')
#to_addr = input('To: ')
#to_name = input('FriendName: ')
#smtp_server = input('SMTP server: ')
#heading = input('Heading: ')
#main_body = input('Main body: ')
from_addr = 'xxxx@xxxx.com'
from_name = 'guy'
password = 'xxxxx'
#hehe, this is my email
to_addr = 'zdyx0379@163.com'
to_name = 'zhaodan'
smtp_server = 'smtp.qq.com'
heading = 'For my friend'
#text email body
main_body_text = 'i miss you, old friend'
#html email body, say hello and show a picture
main_body_html = '<html>'+\
            '<body>'+\
            '<h1>hello, friend</h1>'+\
            '<p><img src="cid:0"></p>'+\
            '</body>'+\
            '</html>'
from_attr = from_name + ' < ' + from_addr + ' > '
to_attr = to_name + ' < ' + to_addr + ' > '

#email.mime.multipart can include accessory
#email.mime.text only support text, we can add email.mime.text to email.mime.multipart by attach method
msg = MIMEMultipart('alternative')
#msg.attach(MIMEText(main_body, 'plain', 'utf-8'))
msg.attach(MIMEText(main_body_html, 'html', 'utf-8'))
#email to be send is a list, here
msg['From'] = _format_addr(from_attr)
msg['To'] = _format_addr(to_attr)
msg['Subject'] = Header(heading, 'utf-8').encode()
with open('E:\\1.jpg', 'rb') as f:
           mime = MIMEBase('image', 'jpg', filename = '1.jpg')
           mime.add_header('Context-Disposition', 'attachment', filename = '1.jpg')
           #set cid of html, then can show img in mail body by html refrence to cid:0
           mime.add_header('Content-ID', '<0>')
           mime.add_header('X-Attachment-ID', '0')
           mime.set_payload(f.read())
           encoders.encode_base64(mime)
           msg.attach(mime)

#add a text email, just in case reciver can't parse html email
msg.attach(MIMEText(main_body_text, 'plain', 'utf-8'))
server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
server.connect(smtp_server, 25)
server.helo()
server.ehlo()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
