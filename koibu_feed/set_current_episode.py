from argparse import ArgumentParser
from search_episodes import get_episodes, get_url_for


def get_current_episodes(episode_data_file):
    current_episodes = {}
    with open(episode_data_file, 'r') as f:
        for line in f.readlines():
            if line:
                title, number = line.strip().split(',')
                current_episodes[title] = number
    return current_episodes

def save_current_episodes(episode_data_file, episodes):
    with open(episode_data_file, 'w') as f:
        for campaign in episodes:
            f.write(f'{campaign},{episodes[campaign]}\n')

def print_current_episodes_info(episodes):
    print('Your new current episodes')
    for campaign, number in episodes.items():
        print('   {:20} - {}'.format(campaign, number))

def set_current_episode(campaign, episode_number, episode_data_file):
    if not episode_number:
        episode_number = len(list(get_episodes(get_url_for(campaign))))
    episodes = get_current_episodes(episode_data_file)
    episodes[campaign] = episode_number
    print_current_episodes_info(episodes)
    save_current_episodes(episode_data_file, episodes)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', dest='campaign', help='Active campaign to set current episode')
    parser.add_argument('-ed', '--episode_data', help='CSV file with the watched episode number', default='../data/current_episode.csv')
    parser.add_argument('-n', dest='episode_number', help='Episode number to be set', type=int)
    args = parser.parse_args()

    set_current_episode(args.campaign, args.episode_number, args.episode_data)