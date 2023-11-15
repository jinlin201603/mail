import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.request
import sys


def get_html(url):
    html = urllib.request.urlopen(url).read()
    return html

def send_email(receiver, subject, url):

    # 163邮箱服务器地址
    mail_host = 'smtp.126.com'
    # 163用户名
    mail_user = 'jinlin201603'
    # 密码(部分邮箱为授权码)
    mail_pass = 'XWIEDGVDUVGRTHCA'
    # 邮件发送方邮箱地址
    sender = mail_user + '@126.com'
    # 邮件接受方邮箱地址
    receivers = [receiver]

    # 邮件内容设置
    # message = MIMEText('海海都知道了','plain','utf-8')
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = subject
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # with open('驿路梨花.html', 'r', encoding='utf-8') as f:
    #     content = f.read()

    content = get_html(url)

    # 设置html格式参数
    part1 = MIMEText(content, 'html', 'utf-8')
    # part2 = MIMEText('海海都知道了', 'plain', 'utf-8')
    message.attach(part1)
    # message.attach(part2)
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        return 'success'
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
        return 'error'

if __name__=='__main__':
    send_email('5909569@qq.com', "随便打", sys.argv[1])