# Programmer: Rizon Takabe
# Class: CS 240
# Date: 4/22/23
# Assignment: Recursive Binary Search

def main():
    array = selection_sort(read_file("numbers-3.txt"))

    right = len(array) - 1
    left = 0
    target = 5842193

    index, operations = binary_search(array, target, left, right)
    if index:
        print(f"Target {target} found at index {index}. Operations: {operations}")
    else:
        print(f"Target {target} not found. Operations: {operations}")

def binary_search(array, target, left, right, operations=0):
    # left and right indexes and operations counter

    if left > right:
        return None, operations

    mid = (left + right) // 2
    operations += 1

    if array[mid] == target:
        return mid, operations
    elif array[mid] > target: 
        return binary_search(array, target, left, mid-1, operations)
    else:
        return binary_search(array, target, mid+1, right, operations)
    

# copy the text files array to an array
def read_file(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append(int(line))
    return array

# returns index of smallest number in array
def find_smallest_num(array):
    smallest_num = array[0]
    smallest_num_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest_num:
            smallest_num = array[i]
            smallest_num_index = i
    return smallest_num_index

# removes the smallest number in unsorted array and adds it to new array
def selection_sort(array):
    new_array = []

    for i in range(len(array)):
        smallest_num = find_smallest_num(array)
        new_array.append(array.pop(smallest_num))
    return new_array

main()
