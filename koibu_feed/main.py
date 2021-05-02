from argparse import ArgumentParser

from episode import Episode
from search_episodes import find_active_campaigns, get_episodes


def main(args):
    titles, urls = find_active_campaigns()
    titles_lower = [t.lower() for t in titles]
    if args.campaign.lower() in titles_lower:
        idx = titles_lower.index(args.campaign)
        episodes = get_episodes(urls[idx])
        episodes = [Episode.from_soup(ep) for ep in episodes]
        for episode in episodes:
            print(episode)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', dest='campaign', help='Active campaign name to look episodes for')
    args = parser.parse_args()

    main(args)    