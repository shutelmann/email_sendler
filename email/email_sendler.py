import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_message = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'shutelmann'
email['to'] = 'sozaev.azamat@outlook.com'
email['subject'] = 'test email'

email.set_content(html_message.substitute({'name': 'Azamat'}), 'html')

with smtplib.SMTP(host='smtp.rambler.ru', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('sickclick@rambler.ru', '@Poe763Com366!')
  smtp.send_message(email)
  print('done')