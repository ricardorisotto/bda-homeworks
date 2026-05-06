data = [10, 20, 30, 40, 50]

count = 0
for item in data:
    count += 1

print(count)

from exercise_01_02_lib import my_len

print(my_len([10, 20, 30]))


data = [10, 20, 30, 40, 50]

total = 0
for item in data:
    total += item
print(total)

data = [10, 20, 30, 40, 50]

# We use `pointer` as an index counter (starting at 0).
pointer = 0
for item in data:
    if item == 30:
        print(pointer)
        break
    pointer += 1

data = [10, 20, 30, 40, 50]

for i in range(len(data)):
    print(i)

matrix = [
    [10, 20],
    [30, 40]
]

for row in matrix:
    print(row)
    for value in row:
        print(value)

# The above function has time complexity O(n*m) 
# where n is the number of rows and m is the number of columns in the matrix. 
# In the worst case, it will check every element in the matrix once.
# The space complexity is O(1) since we are only using a constant amount of extra space for the loop variables and print statements.

matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    # Reset col_index for each new row.
    col_index = 0
    row_index += 1

matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    # Reset col_index for each new row.
    col_index = 0
    row_index += 1    

# The above function has time complexity O(n*m) 
# where n is the number of rows and m is the number of columns in the matrix. 
# In the worst case, it will check every element in the matrix once.
# The space complexity is O(1) since we are only using a constant amount of extra space for the indices and print statements.

arr = [30, 6, 9, 12, 15, 8]

def count_elements(arr):
    count = 0
    for item in arr:
        count += 1
    return count

print("count_elements(arr): ", count_elements(arr))

# The above function has time complexity O(n) where n is the number of elements in the array. 
# In the worst case, it will check every element in the array once. 
# The space complexity is O(1) since we are only using a constant amount of extra space for the count variable.

def sum_even_numbers(arr):
    total = 0
    for item in arr:
        if item % 2 == 0:
            total += item
    return total

print("sum_even_numbers(arr): ", sum_even_numbers(arr))

# The above function has time complexity O(n) where n is the number of elements in the array. 
# In the worst case, it will check every element in the array once (if all elements are even). 
# The space complexity is O(1) since we are only using a constant amount of extra space for the total variable.

def find_first_equal_to_12(arr):
    index = 0
    for item in arr:
        if item == 12:
            return index
        index += 1
    return -1

print("find_first_equal_to_12(arr): ", find_first_equal_to_12(arr)) 

# The above function has time complexity O(n) where n is the number of elements in the array. 
# In the worst case, it will check every element in the array once (if 12 is not present or is the last element). 
# The space complexity is O(1) since we are only using a constant amount of extra space for the index and return value.

matrix = [
    [5, 10, 15],
    [20, 25, 30]
]

def find_coordinates_of_25(matrix):
    row_index = 1
    col_index = 1
    for row in matrix:
        for value in row:
            if value == 25:
                return (row_index, col_index)
            col_index += 1
        # Reset col_index for each new row.    
        col_index = 1
        row_index += 1
    return None

print("find_coordinates_of_25(matrix): ", find_coordinates_of_25(matrix))

# The above function can be simplified by using `enumerate` to track row and column indices:
def find_coordinates_of_25(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == 25:
                return (row_index+1, col_index+1)  # Adding 1 to convert from 0-based to 1-based indexing.
    return None

print("find_coordinates_of_25(matrix): ", find_coordinates_of_25(matrix))

# The above function has time complexity O(n*m) 
# where n is the number of rows and m is the number of columns in the matrix. 
# In the worst case, it will check every element in the matrix once.
# The space complexity is O(1) since we are only using a constant amount 
# of extra space for the indices and return value.
