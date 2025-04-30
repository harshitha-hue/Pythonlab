def remove_char(s, char):
    return s.replace(char, '')
string_input = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
result = remove_char(string_input, char_to_remove)
print(f"String after removing '{char_to_remove}': {result}")
