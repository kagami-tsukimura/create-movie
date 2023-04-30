# Image Crawler

## Overview

This is a Python program to crawl images using the icrawler package.

## Arguments

- `--output`: The output directory for downloaded images. Defaults to `./images`.
  - Shorten: `-o`
- `--N`: The number of images to download. Defaults to `10`.
  - Shorten: `-n`
- `--engine`: The search engine to use. Currently supports `bing` and `google`. Defaults to `google`.
  - Shorten: `-e`

## Development environment

- Python 3.x
- icrawler

## Install

Execute the following command and install the necessary packages.

```bash:pip
pip install icrawler
```

```bash:conda
conda install -c hellock icrawler
```

## How to run

1. Clone the repository

   ```bash:
   git clone https://github.com/kagami-tsukimura/create_movie.git
   ```

1. For the `pip` execution environment, import the following as needed.

   ```bash:
   pip install -r ./environ/requirements.txt
   ```

1. Edit the `./configs/search.txt` file to include the keywords you want to search for.
1. Run the program by executing.

   ```bash:
   python3 crawling.py
   ```
