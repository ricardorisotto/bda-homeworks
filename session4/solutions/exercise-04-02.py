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
    # item will be a tuple: (index, url)
    # Download the image from url, save it to disk, rotate it, 
    # and save the rotated version to disk with a different name
    index, url = item
    filename = f"images/image_{index}.jpg"
    rotated_filename = f"processed/rotated_image_{index}.jpg"
    # Download the image
    urllib.request.urlretrieve(url, filename)
    # Open the image and rotate it 90 degrees
    img = Image.open(filename)
    img = img.rotate(90)
    # Save the rotated image
    img.save(rotated_filename)
    print(f"Downloaded {url} to {filename} and rotated to {rotated_filename}")


def serial_runner(urls):
    start = time.perf_counter()
    # call download_and_rotate() for each url in urls
    for i, url in enumerate(urls):
        download_and_rotate((i, url))
    end = time.perf_counter()
    print(f"\n*** Serial time: {end - start:.2f}s ***\n")


def pool_runner(urls, workers=4):
    start = time.perf_counter()
    # create a pool of workers and call download_and_rotate() for each url in urls
    with mp.Pool(processes=workers) as pool:
        # create tasks as tuples of (index, url) for each url in urls
        # tasks = [(i, url) for i, url in enumerate(urls)] # alternative way to create tasks
        tasks = enumerate(urls)
        pool.map(download_and_rotate, tasks)
    end = time.perf_counter()
    print(f"\n*** Pool time: {end - start:.2f}s ***\n")


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)

    serial_runner(image_urls)
    pool_runner(image_urls, workers=4)

# Pool.map(..) is simpler than creating and managing processes manually, 
# as you don't have to worry about starting and joining processes, 
# and it handles the distribution of tasks across the worker processes for you.

# Files have to have unique names, as otherwise they would overwrite each other 
# when downloaded and processed in parallel.
# So we use the index of the url in the list with the enumerate() function to create unique filenames 
# for the downloaded and processed images.

# Downloading images is quite slow so processing images in parallel is faster 
# than doing it serially. In addition, the processing is independent for each image, 
# so it can be easily parallelized without any issues of shared state or synchronization.