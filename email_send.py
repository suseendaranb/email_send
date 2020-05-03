import smtplib # smtp is the protocol for email communication
#simple mail transfer protocol
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'susai baba'
email['to'] = 'sahanag33@gmail.com'
email['subject'] = 'You found a Parcel'

email.set_content('The Parcel is from pondy')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('suseendaranb@gmail.com','jothibabususee6')
	smtp.send_message(email)
	print('all good boss!')