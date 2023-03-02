import smtplib

smtpServer="webmail.benmann.net"
fromAddr="0034120@jwacs.wa.edu.au"
toAddr="mark@benmann.net"
text="THIS IS TESTING PYTHON EMAIL"
server = smtplib.SMTP(smtpServer,465)
server.ehlo()
#server.starttls()
server.sendmail(fromAddr, toAddr, text)
server.quit()
