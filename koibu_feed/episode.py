base_url = 'https://regalgoblins.fandom.com'

class Episode:
    def __init__(self, title, wiki_link=None, youtube_link=None, twitch_link=None, reddit_link=None):
        self.title = title
        self.wiki_link = wiki_link
        self.youtube_link = youtube_link
        self.twitch_link = twitch_link
        self.reddit_link = reddit_link

    def __str__(self):
        return f'Episode[title={self.title}, wiki_link={self.wiki_link}]'

    @staticmethod
    def from_soup(episode_div):
        main_episode_info = episode_div.contents[3]
        
        title_a = main_episode_info.contents[0]
        title = str(title_a.string)
        try:
            wiki_link = base_url + title_a['href']
        except TypeError:
            wiki_link = None

        return Episode(title, wiki_link)

        