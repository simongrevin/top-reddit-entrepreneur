import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'topredditentrepreneur'}
r = requests.get('https://www.reddit.com/r/Entrepreneur/top/?sort=top&t=week', headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

for link in soup.find_all('a', class_="title")[0:10]:
    print("################")
    print(link.text)
    print('https://www.reddit.com/' + link.get('href'))