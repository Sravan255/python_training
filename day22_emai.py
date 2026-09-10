import smtplib 
from email.message import EmailMessage

# simple message
sender = 'rakkeshadithya00@gmail.com' 
password = 'silglmwkmtqxybct'
receiver = 'wd.rkad@gmail.com' 
message = 'Hi rakesh, I have sent this mail from python code' 
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.sendmail(sender, receiver, message)
print('Message sent successfully')


# message with Subject and attachments
sender = 'rakkeshadithya00@gmail.com' 
password = 'silglmwkmtqxybct'
message = EmailMessage()
message['From'] = 'rakkeshadithya00@gmail.com'
message['To'] = 'wd.rkad@gmail.com'
message['Subject'] = 'SMTP MAIL'
message.set_content('Hi Rakesh, Iam sending this mail from Python Code')
files = ['file_handling.png', 'php_record.pdf']
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')



# Bulk mail sending with Subject and attachments
sender = 'rakkeshadithya00@gmail.com' 
password = 'silglmwkmtqxybct'
receivers = ['wd.rkad@gmail.com', 'rakesh@codegnan.com']
message = EmailMessage()
message['From'] = 'rakkeshadithya00@gmail.com'
message['Bcc'] = ','.join(receivers)
message['Subject'] = 'SMTP MAIL'
message.set_content('Hi Rakesh, Iam sending this mail from Python Code')
files = ['file_handling.png']
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')