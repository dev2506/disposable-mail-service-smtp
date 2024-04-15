import smtplib

server = smtplib.SMTP('127.0.0.1', 25)
server.sendmail("test@example.com", ["test@foryou.com"], 'Test123')

server.quit()