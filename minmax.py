def find_min_max(lst):
    if not lst:
        return None, None
    min_val = lst[0]
    max_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val
my_list = [10, 3, 5, 8, 2]
min_num, max_num = find_min_max(my_list)
print("Minimum:", min_num, "Maximum:", max_num)
