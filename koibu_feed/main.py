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
        episode_number = get_episode_watched(args.campaign, args.episode_data)
        for i, episode in enumerate(episodes):
            if i == episode_number:
                print('========== New Episodes Below ==========')
            episode.print_episode_info()


def get_episode_watched(campaign, current_episode_file):
    with open(current_episode_file, 'r') as f:
        for line in f.readlines():
            campaign_title, episode_number = line.split(',')
            if campaign.lower() == campaign_title.lower():
                return int(episode_number)
    return 0

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', dest='campaign', help='Active campaign name to look episodes for')
    parser.add_argument('-ed', '--episode_data', help='CSV file with the watched episode number', default='../data/current_episode.csv')
    args = parser.parse_args()

    main(args)