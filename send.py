import smtplib

server = smtplib.SMTP('13.234.38.143', 587)
server.sendmail("test@example.com", ["test@foryou.com"], 'Test123')

server.quit()