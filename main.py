import requests
from bs4 import BeautifulSoup
import smtplib
import configparser
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

headers = {'user-agent': 'topredditentrepreneur'}
response = requests.get('https://www.reddit.com/r/Entrepreneur/top/?sort=top&t=week', headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

body = ""
for link in soup.find_all('a', class_="title")[0:10]:
    body += '################'
    body += link.text
    body += 'https://www.reddit.com/' + link.get('href')


# Get the config
config = configparser.ConfigParser()
config.read('/Users/simongrevin/Documents/dev/top-reddit-entrepreneur/mail.conf')



fromaddr = config['EMAIL']['From']
toaddr = config['EMAIL']['To']
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "/r/Entrepreneur Top 10 of the week"
msg.attach(MIMEText(body, 'plain'))

# Gmail SMTP credentials
username = config['AUTH']['Username']
password = config['AUTH']['Password']

# Send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()





 

