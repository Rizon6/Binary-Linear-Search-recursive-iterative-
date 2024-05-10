def main():
    array = file_read("numbers-3.txt")
    target = 808995
    i = 0
    answer = recursive_search(array, target, i)
    if answer:
        print("Target", target, "found at position", answer)
    else:
        print("Target not found")

def recursive_search(array, target, i):
    if i >= len(array): # base case
        return None
    elif array[i] == target: # base case
        return i
    else:
        return recursive_search(array, target, i+1) # recursive case
    
def file_read(file):
    array = []
    with open(file, 'r') as file:
        for line in file:
            array.append(int(line))
    return array

main()
