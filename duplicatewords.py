sentence = "the sky is blue and the grass is green"
words = sentence.split()

has_duplicates = len(words) != len(set(words))
print("Has duplicate words?" , has_duplicates)
