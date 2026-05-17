"""Session 4 Homework: Two-Sum Problem

The Problem: 
Given a sorted array of integers and a target integer z, determine if there are two distinct numbers in the array that sum to z.

The Solution:
We are looking for a function that has two arguments: 
    arr - an array of integers sorted in ascending order
    z - an integer
The function returns a boolean which is true if there is a pair of numbers in the array
that add up to the integer z. The integers can be positive or negative or zero.

The method I propose to solve this as follows:
1) Add up the first 2 integers in the array. If they add up to more than z, then since they are the smallest in the array, 
the function should return false.

2) Add up the last 2 integers in the array. If they add up to less than z, then since they are the largest in the array, 
the function should return false. 

3) If not cases 1) and 2) proceed as follows: 

Let's call the left hand side of the array the first (smallest) element of array onwards, 
and the right hand side the last (largest) element of the array.

We can incremeentally work towards a solution by starting with the smallest and largest integers in the array, at either end of the array, 
and then moving towards a sum closer to z by incrementing from either end of the array, depending on whether the sum of the two integers is
 less than or greater than z:
  -  If it is greater than z, then we need to try a smaller sum which can only be done by 
 moving leftwards from the right hand side to a smaller integer. 
  - If it is less than z, then we need to try a larger sum which can only be done by 
 moving rightwards from the left hand side to a larger integer.

So the process is as follows:

Add the first and last elements of the array. 
If their sum is less than z then proceed from the left hand side trying each element until the sum is greater than or equal to z. 
If at any point the sum is greater than z then proceed from the right hand side of the array trying each element 
until the sum is less than or equal to z. Continue in this fashion until one of the following:

    a) you have found a sum equal to z (in which case return true) 

    b) when proceeding from the left, the index of the array that you have reached is greater than or equal to 
    the index of the array you last reached when proceeding from the right. In that case no sum equal to z was found so return false.

    c) when proceeding from the right, the index of the array that you have reached is greater than or equal to 
    the index of the array you last reached when proceeding from the left. In that case no sum equal to z was found so return false.

    The time complexity of this algorithm is O(n) where n is the length of the array, since in the worst case we have to check each element of the array once.

    The space complexity of this algorithm is O(1) since we only need a constant amount of extra space to keep track of the indices and the current sum.
    
"""

def has_pair_with_sum(arr, z):
    """
    Determines whether a sorted array contains a pair of integers that sum to z.

    Args:
        arr: A list of integers sorted in ascending order.
        z:   The target sum (may be negative, zero, or positive).

    Returns:
        True if any two distinct positions in arr hold values that sum to z,
        False otherwise.
    """
    print(f"\nChecking array: {arr} for pair sum: {z}")

    n = len(arr)

    # Need at least two elements to form a pair.
    if n < 2:
        return False

    # Step 1: If the two smallest elements already exceed z,
    # no pair in the array can possibly sum to z.
    if arr[0] + arr[1] > z:
        print("Early exit: two smallest elements exceed z.")
        return False

    # Step 2: If the two largest elements still fall short of z,
    # no pair in the array can possibly sum to z.
    if arr[-1] + arr[-2] < z:
        print("Early exit: two largest elements less than z.")
        return False

    # Step 3: Two-pointer sweep from both ends toward the middle.
    left, right = 0, n - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == z:
            print(f"Found pair: {arr[left]} + {arr[right]} = {z}")
            return True
        elif current_sum < z:
            # Sum too small — advance left to try a larger value.
            # If this push makes left meet/cross right, the loop exits
            # and we fall through to return False (your termination case b).
            left += 1
        else:
            # Sum too large — retreat right to try a smaller value.
            # If this pull makes right meet/cross left, the loop exits
            # and we fall through to return False (your termination case c).
            right -= 1

    print("No pair found that sums to z.")
    return False


if __name__ == "__main__":
    test_cases = [
        # (arr, z, expected)
        ([1, 2, 3, 4, 5],      7,   True),   # 2+5 or 3+4
        ([1, 2, 3, 4, 5],      9,   True),   # 4+5
        ([1, 2, 3, 4, 5],     10,   False),  # step 2 early exit
        ([1, 2, 3, 4, 5],      2,   False),  # step 1 early exit
        ([-5, -2, 0, 3, 6],    1,   True),   # -2+3
        ([-5, -2, 0, 3, 6],    4,   True),   # -2+6
        ([-5, -2, 0, 3, 6],    2,   False),  # no pair sums to 2
        ([-3, -1, 0, 1, 3],    0,   True),   # -3+3 or -1+1
        ([0, 0],               0,   True),   # 0+0
        ([0, 0, 0, 0],         0,   True),
        ([-10, -5, 0, 5, 10], -15,  True),   # -10+-5
        ([-10, -5, 0, 5, 10],-100,  False),  # step 1 early exit (negative z)
        ([-10, -5, 0, 5, 10], 100,  False),  # step 2 early exit
        ([5],                  5,   False),  # too short
        ([],                   0,   False),  # empty
        ([1, 1, 1, 1],         2,   True),   # 1+1
        ([1, 1, 1, 1],         3,   False),
         ([-5, -2, 0, 3, 6, 12, 13, 14, 17, 20, 21],    2,   False),  # no pair sums to 2 (longer array)
         ([-5, -2, 0, 3, 6, 12, 13, 14, 17, 20, 21],    7,   True),  # 13 - 5 (longer array)
    ]

    all_pass = True
    for arr, z, expected in test_cases:
        result = has_pair_with_sum(arr, z)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_pass = False
        print(f"TEST {status}: has_pair_with_sum({arr}, {z}) = {result}  (expected {expected})")

    print()
    print("ALL TESTS PASSED" if all_pass else "SOME TESTS FAILED")