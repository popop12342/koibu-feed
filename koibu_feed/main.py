from argparse import ArgumentParser

from episode import Episode
from search_episodes import find_active_campaigns, get_episodes


if __name__ == '__main__':
    titles, urls = find_active_campaigns()
    episodes = get_episodes(urls[0])
    episodes = [Episode.from_soup(ep) for ep in episodes]
    for episode in episodes:
        print(episode)
