# 🎵 Async Music Handler

A lightweight asynchronous CLI tool for downloading audio from URLs supported by [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

The project combines `asyncio` with worker threads to download multiple tracks concurrently while limiting the number of simultaneous downloads.

> **Status:** personal learning project / experimental tool.

## ✨ Features

* 🎧 Download audio from URLs supported by **yt-dlp**
* ⚡ Concurrent downloads using `asyncio`
* 🧵 Run blocking `yt-dlp` operations in worker threads
* 🚦 Configurable number of concurrent workers
* 📊 Progress bar with `tqdm`
* ⚙️ JSON-based configuration
* 📁 Configurable download directory
* ✅ Track successfully downloaded URLs
* ❌ Track failed URLs
* ⏱️ Execution-time measurement
* 🖥️ Command-line interface

## 🧠 Architecture

The application uses `asyncio` for orchestration while moving blocking download operations to worker threads.

```text

                         URLs
                          │
                          ▼
                  ┌───────────────┐
                  │    asyncio    │
                  │     tasks     │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   Semaphore   │
                  │  worker limit │
                  └───────┬───────┘
                          │
                          ▼
                 asyncio.to_thread()
                          │
                          ▼
                      yt-dlp
                     /     \
                    /       \
                   ▼         ▼
              successful   failed
```

The semaphore limits the number of downloads running simultaneously, while `asyncio.to_thread()` prevents blocking `yt-dlp` calls from blocking the event loop.

## 🛠️ Tech Stack

* **Python 3.14+**
* **asyncio**
* **yt-dlp**
* **tqdm**
* **argparse**
* **JSON**
* **uv**
* **FFmpeg**

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Giorgi61/async_music_handler.git
cd async_music_handler
```

Install dependencies:

```bash
uv sync
```

### FFmpeg

FFmpeg is required for audio extraction and conversion.

Check that it is installed:

```bash
ffmpeg -version
```

## 🚀 Usage

The main entry point is:

```bash
python async_music/main.py
```

### Download songs

Pass one or more URLs with `-s` / `--song-urls`:

```bash
python async_music/main.py \
    -s "https://example.com/song1" \
       "https://example.com/song2"
```

### Change the download directory

```bash
python async_music/main.py \
    -s "https://example.com/song" \
    -dd "../downloads"
```

### Change the number of workers

```bash
python async_music/main.py \
    -s "https://example.com/song1" "https://example.com/song2" \
    -w 8
```

The default number of workers is `4`.

### Use a custom configuration

```bash
python async_music/main.py \
    -s "https://example.com/song" \
    -c ./config.json
```

## ⚙️ Configuration

The default configuration is stored in:

```text
async_music/config.json
```

Example:

```json
{
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320"
        }
    ],
    "prefer_ffmpeg": true,
    "quiet": true
}
```

The application also configures the output template:

```text
%(title).80s.%(ext)s
```

This means downloaded files use the media title as their filename.

## 📁 Project Structure

```text
async_music_handler/
│
├── async_music/
│   ├── main.py
│   ├── async_downloader.py
│   ├── music_handler.py
│   ├── cli_parser.py
│   ├── PrettyQueue.py
│   ├── script_utils.py
│   ├── config.json
│   │
│   └── ejs/
│       └── ...
│
├── LICENSE
├── README.md
└── ...
```

### Core modules

| Module                | Responsibility                                       |
| --------------------- | ---------------------------------------------------- |
| `main.py`             | Application entry point and high-level orchestration |
| `async_downloader.py` | Asynchronous task scheduling and concurrency control |
| `music_handler.py`    | `yt-dlp` integration and individual downloads        |
| `cli_parser.py`       | Command-line argument parsing                        |
| `PrettyQueue.py`      | Queue wrapper with custom representation             |
| `script_utils.py`     | Utility functions and decorators                     |
| `config.json`         | `yt-dlp` configuration                               |

## 🔄 Concurrency Model

`yt-dlp` performs blocking operations, so the project does not attempt to make `yt-dlp` itself asynchronous.

Instead, downloads are executed in worker threads:

```python
await asyncio.to_thread(
    music_handler.download_one_song,
    song_url,
    config
)
```

The number of concurrent downloads is controlled with an `asyncio.Semaphore`:

```python
async with semaphore:
    ...
```

This gives the application an asynchronous orchestration layer while allowing blocking download operations to run outside the event loop.

## 📊 Progress Tracking

The application uses `tqdm` together with `asyncio.as_completed()` to display download progress as individual tasks finish.

At the end of the process, successful downloads and failed URLs are reported separately.

## ⚠️ Current Limitations

This project is primarily a learning and experimentation project rather than a production-ready application.

Current limitations include:

* minimal error handling
* no retry mechanism
* no persistent download database
* no resume system for interrupted downloads
* minimal configuration validation
* dependency on `yt-dlp` and FFmpeg
* CLI and internal architecture are still evolving

## 🎯 Purpose

The main purpose of this project is to explore practical Python concepts through a real application rather than to build a production-grade music downloader.

The project provided practice with:

* asynchronous programming with `asyncio`
* concurrency and worker threads
* `asyncio.Semaphore`
* `asyncio.to_thread()`
* handling blocking operations inside asynchronous applications
* CLI design with `argparse`
* decorators
* type annotations
* configuration management
* third-party library integration
* progress tracking

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

See the [LICENSE](./LICENSE) file for the full license text.

