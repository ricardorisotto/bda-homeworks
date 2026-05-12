numbers = [1, 2, 3]

for number in numbers:
    print(number)

# Using an explicit iterator
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# Using an explicit iterator with a file
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    it = iter(file)
    print(next(it))
    print(next(it))

# Using an explicit iterator with a file (alternative)
TEXT_FILE = "les_miserables.txt"
with open(TEXT_FILE, "r", encoding="utf-8") as file:
    # Provide here your solution
    print(next(file, ""))

# Using a for loop with a file to find a specific line
TEXT_FILE = "les_miserables.txt"
target = "Jean Valjean"
found = None

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        if target in line:
            found = line
            break

print(found)

# Counting the number of lines in a file using a for loop
TEXT_FILE = "les_miserables.txt"
count = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print(count)

# Counting the number of lines containing a specific word using a for loop
TEXT_FILE = "les_miserables.txt"
target = "Jean"

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

count = 0

for line in non_empty_lines(TEXT_FILE):
    if target in line:
        count += 1

print(count)