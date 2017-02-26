import requests
from bs4 import BeautifulSoup
import smtplib
import configparser
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import sys


if len(sys.argv) != 2:
    print("Need mail.conf path in argument")
    sys.exit()
else:
    path = sys.argv[1]
    # Get the config from mail.conf
    config = configparser.ConfigParser()
    config.read(path)

# get the content from reddit.com
headers = {'user-agent': 'topredditentrepreneur'}
response = requests.get('https://www.reddit.com/r/Entrepreneur/top/?sort=top&t=week', headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

#subject and title
today = datetime.date.today()
subject = 'Top 10 /r/Entrepreneur, {}'.format(today.strftime('%d %b %Y'))

body = '<h1>' + subject + '</h1>'
body += '<br />'

# writing the email
for link in soup.find_all('a', class_="title")[0:10]:
    body += '<a href="{}">{}</a>'.format('https://www.reddit.com/' + link.get('href'), link.text)
    body += '<br /><br />'

# Setting the email
fromaddr = config['EMAIL']['From']
recipients = config['EMAIL']['To'].split(',')

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

# Gmail SMTP credentials
username = config['AUTH']['Username']
password = config['AUTH']['Password']

# Send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, recipients, msg.as_string())
server.quit()

print("mail sent")
