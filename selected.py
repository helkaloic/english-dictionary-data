import json
import os

filtered_json = {}
select_words = []

print("Read the files...")

# Read google-10000-english-no-swears.txt file
with open(os.path.join("text", "selected.txt"), "r") as select_file:
    select_words = [x.strip().lower() for x in select_file.readlines()]

# Read filtered.json file
with open(os.path.join("processed", "filtered.json"), "r") as filtered_file:
    contents = filtered_file.read()
    filtered_json = json.loads(contents)
    
print("Filter words...")

# Create a new dictionary to store selected words
selected_json = {}

# Iterate through filtered.json and select only meaningful words
for word, data in filtered_json.items():
    if word.lower() in select_words:
        selected_json[word] = data

print("Seleted words (json): ", len(selected_json), "words")

# Write the selected dictionary to selected.json
with open(os.path.join("processed", "selected.json"), "w") as output_file:
    output_file.write(json.dumps(selected_json))

print("Wrote out processed/selected.json")
