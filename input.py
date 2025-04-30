import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Array:", my_array)
print("First element:", my_array[0])
print("Last element:", my_array[-1])
doubled_array = my_array * 2
print("Array after doubling each element:",doubled_array)
