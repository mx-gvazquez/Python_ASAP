def find_odd_occurrence(arr):
    result = 0
    for number in arr:
        result ^= number
    return result
# Example usage:
arr = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
print("The number that appears an odd number of times is:", find_odd_occurrence(arr))