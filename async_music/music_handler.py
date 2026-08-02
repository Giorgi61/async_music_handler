import json
from typing import Mapping, Any
from pathlib import Path

from yt_dlp import YoutubeDL

from PrettyQueue import PrettyQueue

ERRORED_URLS: PrettyQueue[str] = PrettyQueue()
SUCCESSED_URLS: PrettyQueue[str] = PrettyQueue()


def load_config(conf_path_json: str | Path, download_dir:  Path) -> dict:
    with open(conf_path_json, "r", encoding='utf-8') as f:
        settings = json.load(f)

    settings["outtmpl"] = str(download_dir / "%(title).80s.%(ext)s")

    return settings


def download_one_song(url: str, config: Mapping[str, Any]):
    with YoutubeDL(config) as ydl:
        try:

            ydl.download([url])
            SUCCESSED_URLS.put(url, block=True)
        except Exception as e:
            ERRORED_URLS.put(url, block=True)
            print(repr(e))
