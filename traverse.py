def reverse_traverse(lst):
    length = len(lst)
    for i in range(length - 1, -1, -1):
        print(lst[i])
original_list = ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
reverse_traverse(original_list)
