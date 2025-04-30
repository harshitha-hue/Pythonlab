def split_list(lst, first_part_length):
    first_part = []
    second_part = []
    for i in range(len(lst)):
        if i < first_part_length:
            first_part.append(lst[i])
        else:
            second_part.append(lst[i])
    return first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3
part1, part2 = split_list(original_list, length_first_part)
print("Splitted list:", (part1, part2))
