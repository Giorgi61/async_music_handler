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

    SONGS = []

    WORKERS = args.workers

    main(SONGS, CONFIG_PATH, DOWNLOAD_DIR, WORKERS)
