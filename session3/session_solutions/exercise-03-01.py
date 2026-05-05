"""Session 3 Exercise 1 reference solution: streaming vs loading text data.

Run from the session3 folder:
    python3 session_solutions/exercise-03-01.py

Download the data first:
    hf download Birkbeck/les-miserables-txt les_miserables.txt --repo-type dataset --local-dir .
"""

TEXT_FILE = "les_miserables.txt"
SEARCH_TEXT = "Jean Valjean"


def first_line(path):
    """Return the first line of a text file."""
    with open(path, "r", encoding="utf-8") as file:
        return next(file).rstrip("\n")


def find_first_match(path, target):
    """Return the first line containing target, or None if not found."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if target in line:
                return line.rstrip("\n")
    return None


def count_lines_streaming(path):
    """Count all lines without storing them."""
    count = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
    return count


def average_line_length_streaming(path):
    """Compute average line length without storing all lines."""
    total_length = 0
    count = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            total_length += len(line)
            count += 1

    if count == 0:
        return 0

    return total_length / count


def load_all_lines(path):
    """Load all lines into memory for tasks that need all records at once."""
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


if __name__ == "__main__":
    print("First line:")
    print(first_line(TEXT_FILE))

    print("\nFirst match:")
    print(find_first_match(TEXT_FILE, SEARCH_TEXT))

    print("\nLine count:")
    print(count_lines_streaming(TEXT_FILE))

    print("\nAverage line length:")
    print(average_line_length_streaming(TEXT_FILE))

    print("\nLoaded line count:")
    print(len(load_all_lines(TEXT_FILE)))
