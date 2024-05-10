def main():
    file_arr = file_read("numbers-3.txt")
    target = int(input("Enter an integer: "))
    result = iterative_search(file_arr, target)
    if result:
        print(str(target) + " was found at index " + str(result))
    else:
        print("Target not found")
# loop through array until the element is the target, then return the index of element
# if it gets to end of list without finding it, return none
def iterative_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return None

def file_read(file):
    array = []
    with open(file, 'r') as file:
        for line in file:
            array.append(int(line))
    return array

main()
