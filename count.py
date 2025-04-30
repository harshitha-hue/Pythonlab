def count_char_occurrences(s, char):
    return s.count(char)
string_input = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")
count = count_char_occurrences(string_input, char_to_count)

print(f"The character '{char_to_count}' appears {count} time(s) in the string.")
