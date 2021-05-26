base_url = 'https://regalgoblins.fandom.com'

class Episode:
    def __init__(self, title, wiki_link=None, youtube_link=None, twitch_link=None, reddit_link=None):
        self.title = title
        self.wiki_link = wiki_link
        self.youtube_link = youtube_link
        self.twitch_link = twitch_link
        self.reddit_link = reddit_link

    def print_episode_info(self):
        print(self.title)
        if self.wiki_link:
            print('Wiki    - ', self.wiki_link)
        if self.youtube_link:
            for idx, link in enumerate(self.youtube_link):
                print(f'Youtube {idx+1} - ', link)
        if self.twitch_link:
            for idx, link in enumerate(self.twitch_link):
                print(f'Twitch {idx+1}  - ', link)
        if self.reddit_link:
            for idx, link in enumerate(self.reddit_link):
                print(f'Reddit {idx+1}  - ', link)

    def __str__(self):
        s = f'Episode[title={self.title}'
        if self.wiki_link:
            s += ',wiki_link=' + self.wiki_link
        if self.youtube_link:
            s += ',youtube_link=' + self.youtube_link
        if self.twitch_link:
            s += ',twitch_link=' + self.twitch_link
        if self.reddit_link:
            s += ',reddit_link=' + self.reddit_link
        s += ']'
        return s

    @staticmethod
    def from_soup(episode_div):
        main_episode_info = episode_div.contents[3]
        
        title_a = main_episode_info.contents[0]
        title = str(title_a.string)
        try:
            wiki_link = base_url + title_a['href']
        except TypeError:
            wiki_link = None

        other_links = [a['href'] for a in main_episode_info.find_all('a')]
        youtube_link = _filter_links(other_links, 'youtube.com')
        twitch_link = _filter_links(other_links, 'twitch.tv')
        reddit_link = _filter_links(other_links, 'reddit.com')

        return Episode(title, wiki_link, youtube_link, twitch_link, reddit_link)

def _filter_links(links, substring):
    return list(filter(lambda link: substring in link, links))
