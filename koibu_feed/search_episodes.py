import requests
from bs4 import BeautifulSoup

def find_active_campaigns():
    base_url = 'https://regalgoblins.fandom.com'
    response = requests.get(base_url + '/wiki/Arcadia_Wiki')
    soup = BeautifulSoup(response.content, 'html.parser')

    active_campains_tds = soup.tr.table.find_all('td')
    links = []
    for td in active_campains_tds:
        links.extend(td.find_all('a'))
    
    titles = []
    urls = []
    for link in links:
        titles.append(link['title'])
        urls.append(base_url + link['href'])

    return titles, urls

def is_episode(element):
    if 'style' in str(element):
        return 'width:100%' in element['style']
    return False

def get_episodes(campaign_url):
    response = requests.get(campaign_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    children = soup.article.div.div.div.div.children
    episodes = filter(is_episode, children)
    return episodes
