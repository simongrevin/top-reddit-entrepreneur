import requests

headers = {'user-agent': 'topredditentrepreneur'}
r = requests.get('https://www.reddit.com/r/Entrepreneur/top/?sort=top&t=week', headers=headers)