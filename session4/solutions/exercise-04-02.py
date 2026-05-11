import multiprocessing as mp
import os
import time
import urllib.request

from PIL import Image


image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]


def download_and_rotate(item):
    # item is a tuple: (index, url)
    # TODO
    ...


def serial_runner(urls):
    start = time.perf_counter()
    # TODO
    ...
    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")


def pool_runner(urls, workers=4):
    start = time.perf_counter()
    # TODO
    ...
    end = time.perf_counter()
    print(f"Pool time: {end - start:.2f}s")


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)

    serial_runner(image_urls)
    pool_runner(image_urls, workers=4)
