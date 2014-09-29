import smtplib, email
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _format_addr(s):
    (name, addr) = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr))

from_addr = input('From: ')
from_name = input('MyName: ')
password = input('Password: ')
to_addr = input('To: ')
to_name = input('FriendName: ')
smtp_server = input('SMTP server: ')
heading = input('Heading: ')
main_body = input('Main body: ')
from_attr = from_name + ' < ' + from_addr + ' > '
to_attr = to_name + ' < ' + to_addr + ' > '

msg = MIMEText(main_body, 'plain', 'utf-8')
msg['From'] = _format_addr(from_attr)
msg['To'] = _format_addr(to_attr)
msg['Subject'] = Header(heading, 'utf-8').encode()
    	
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.connect(smtp_server, 25)
server.helo()
server.ehlo()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
