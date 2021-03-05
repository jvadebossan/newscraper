import smtplib
from email.message import EmailMessage

def main(email, msg_nt, notices):
    msg = EmailMessage()
    msg.set_content(msg_nt)
    msg['Subject'] = f'notícias mais recentes sobre {notices}'
    msg['From'] = 'newscraper.jv@gmail.com'
    msg['To'] = email
    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(msg['From'], 'newscraperdojv')
    server.send_message(msg)
    server.quit()