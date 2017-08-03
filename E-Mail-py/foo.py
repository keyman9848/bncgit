from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = r'webmaster@tccxfw.com'  # 发送邮箱用户名
password = 'TCCxfw123'               # 密码
to_addr = r'1938036263@qq.com'       # 发送对象的邮箱地址
smtp_server = r'172.16.254.45'       # 服务器
# 邮件的内容
msg = MIMEText('你好, 信息化工程所关于项目的通知...', 'plain', 'utf-8')

msg['From'] = _format_addr('信息化工程所 <%s>' % from_addr)
msg['To'] = _format_addr('客户 <%s>' % to_addr)
msg['Subject'] = Header('来自信息化工程所的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
# $smtp = new smtp("172.16.254.45",25,true,"webmaster@tccxfw.com","TCCxfw123");
# server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()






# 1938036263@qq.com
# happy1990
# smtp.qq.com
# 584751697@qq.com
# jason123@vip.qq.com
# tukulvgoyexubdad


# beanstalkd

# Array ( [id] => 1 [body] => {to:"meetcd@126.com",subject:"is test",body:"test maill!"} )