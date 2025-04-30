sentence = "the sky is blue and the grass is green"
words = sentence.split()
unique_words = set(words)
if len(words) != len(unique_words):
    print("The sentence has duplicate words.")
else:
    print("The sentence has all unique words.")

