import multiprocessing as mp
import time


def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")
    return f"Task {name} done"


if __name__ == "__main__":
    start = time.perf_counter()

    tasks = ["A", "B", "C", "D"]

    with mp.Pool(processes=4) as pool:
        results = pool.map(task, tasks)

    end = time.perf_counter()

    print(results)
    print(f"Total time: {end - start:.2f}s")