import asyncio

from tqdm.auto import tqdm

import music_handler


async def download_one(song_url, config, semaphore):
    async with semaphore:
        await asyncio.to_thread(music_handler.download_one_song, song_url, config)


async def main(urls: list[str], config, semaphore_size):
    semaphore = asyncio.Semaphore(semaphore_size)

    tasks = [asyncio.create_task(download_one(url, config, semaphore)) for url in urls]

    for task in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc='Downloading songs'):
        await task
