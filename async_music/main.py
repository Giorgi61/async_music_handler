import asyncio
import sys
from pathlib import Path

import music_handler
import async_downloader
import cli_parser
import script_utils


@script_utils.timer
def main(songs, conf_path, dest_path, workers=4):
    config = music_handler.load_config(conf_path, dest_path)

    asyncio.run(async_downloader.main(songs, config, workers))

    errors = music_handler.ERRORED_URLS
    successes = music_handler.SUCCESSED_URLS

    print(f"Total Downloaded: {len(successes)}")

    if count := len(errors):
        print(f"Errors count: {count}", file=sys.stderr)
        print(f"Invalid URLS: {errors}", file=sys.stderr)


if __name__ == "__main__":
    args = cli_parser.parser.parse_args()

    CURRENT_DIR = Path(__file__).resolve().parent
    CONFIG_NAME = args.config
    CONFIG_PATH = CURRENT_DIR / CONFIG_NAME

    DOWNLOAD_DIR = (CURRENT_DIR / args.download_directory / 'music/').resolve()
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    SONGS = args.song_urls

    SONGS = ['https://www.facebook.com/reel/1436503254986208',
             'https://www.facebook.com/groups/189078363976213/permalink/1028037383413636/?rdid=DZ8tKobngQFP49CI#',
             'https://www.facebook.com/reel/1043551384719358', 'https://www.facebook.com/reel/1584458709958299',
             'https://www.facebook.com/reel/2428080981007130', 'https://www.facebook.com/reel/1411612857532116',
             'https://www.facebook.com/reel/1322113523238349', 'https://www.facebook.com/reel/1689039632306039',
             'https://www.facebook.com/reel/27762619203400890', 'https://www.facebook.com/reel/2413833399106043',
             'https://www.facebook.com/reel/27666538142988946', 'https://www.facebook.com/reel/1003591505770217',
             'https://www.facebook.com/reel/2068342883760450', 'https://www.facebook.com/reel/2099142703974549',
             'https://www.facebook.com/reel/2007653230181718', 'https://www.facebook.com/reel/4450010415214733',
             'https://www.facebook.com/reel/1556371216034731', 'https://www.facebook.com/reel/37024779880501836',
             'https://www.facebook.com/reel/2219021775308954', 'https://www.facebook.com/reel/4406945532896487',
             'https://www.facebook.com/reel/3174902532700137', 'https://www.facebook.com/reel/1357454115808964',
             'https://www.facebook.com/reel/1577096687328904', 'https://www.facebook.com/reel/28791167963806455',
             'https://www.facebook.com/groups/771606750055444/permalink/2167876317095140/?rdid=iph9Ex76I676ZG03#',
             'https://www.facebook.com/reel/4590531154604384', 'https://www.facebook.com/reel/1053184683741950',
             'https://www.facebook.com/reel/1724279325557574', 'https://www.facebook.com/reel/1366609522070796',
             'https://www.facebook.com/reel/4573615896219677', 'https://www.facebook.com/reel/1046972954571234']

    WORKERS = args.workers

    main(SONGS, CONFIG_PATH, DOWNLOAD_DIR, WORKERS)
