import requests
from bs4 import BeautifulSoup

#use .titleline instead of .storylink

res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')

def create_custom_hn(link, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        print(points)
        hn.append({'title': title, 'links': href})
    return hn

print(create_custom_hn(links, votes))