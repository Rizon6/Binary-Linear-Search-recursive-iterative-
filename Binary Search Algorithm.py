# Programmer: Rizon Takabe
# Class: CS 240
# Date: 4/4/23
# Assignment: Binary Search

def binary_search(array, target):
    # left and right pointers and operations counter
    left = 0
    right = len(array) - 1
    operations = 0

    while left <= right:
        operations += 1
        mid = (left + right) // 2

        if array[mid] == target:
            return mid, operations
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, operations

# copy the text files numbers to an array
def read_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers

# runs binary_search function for every number in targets array
def main():
    numbers = read_file("numbers.txt")

    targets = [51216352, 198313119, 196614208]

    for target in targets:
        index, operations = binary_search(numbers, target)
        if index != -1:
            print(f"Target {target} found at index {index}. Operations: {operations}")
        else:
            print(f"Target {target} not found. Operations: {operations}")

main()