import os


def read_file_to_set(file_path):
    with open(file_path, "r") as file:
        # Remove leading and trailing whitespaces from each word
        words = {word.strip() for word in file.read().split()}
    return words

# Read 20k_words.txt
words = read_file_to_set(os.path.join("text", "20k_words.txt"))

# Read bad-words.txt
swear_words = read_file_to_set(os.path.join("text", "bad-words.txt"))

# Create selected_words set containing words that are in words but not in swears
selected_words = words.intersection(words - swear_words)

# Write selected_words to selected.txt
with open(os.path.join("text", "selected.txt"), "w") as output_file:
    output_file.write("\n".join(sorted(selected_words)))

print("Selected words (txt): ", len(selected_words), "words")
print("Wrote out text/selected.txt")
