names = ["Alice", "Amanda", "Bob", "Charlie", "Catherine", "David", "Diana", "Eve"]

grouped_names = {}

for name in names:
    first_letter = name[0].upper()  
    if first_letter not in grouped_names:
        grouped_names[first_letter] = []
    grouped_names[first_letter].append(name)


print(grouped_names)
