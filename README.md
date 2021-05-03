# Koibu Feed

Personal feed for Koubus active campains

## Instalation

You should have installed Python 3 and pip.

```bash
pip install -r requirements.txt
```

## Usage

Run main.py file and choose the name of the campaign you want to search.

```bash
cd koibu_feed
python main.py -c "Tombs of Scoria"
```

To mark the current episode you are currently watching use the
[`sample_episode_file.csv`](data/sample_episode_file.csv) file. On each line
add the campaign title and episode number separated by a comma.

To use a different file use

```bash
python main.py -c "Tombs of Scoria" -ed "../data/sample_episode_file.csv"
```

To set the current episodes on the command line use

```bash
python set_current_episode.py -c "Tombs of Scoria" -n 32 -ed "../data/sample_episode_file.csv"
```