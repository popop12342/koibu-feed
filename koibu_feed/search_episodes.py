import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

def find_active_capains():
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

if __name__ == '__main__':
    titles, urls = find_active_capains()
    print(titles)
    print(urls)
