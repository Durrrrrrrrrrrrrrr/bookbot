


def count(text):
	words = text.split()
	return len(words)
with open("books/frankenstein.txt") as f:
	file_contents = f.read()

word_count = count(file_contents)

print(f"The book contains {word_count} words.")

def letter(text):
	letters = {}
	for character in  text:
		character = character.lower()
		if character in letters:
			letters[character] += 1
		else:
			letters[character] = 1
	return letters

letters = letter(file_contents)

sorted_letters = []

for char, count in letters.items():
	sorted_letters.append({"char": char, "num": count})

def sort_on(dict):
	return dict["num"]

sorted_letters.sort(reverse=True, key=sort_on)

print("--Begin report--")

for item in sorted_letters:
	if item["char"].isalpha():
		char = item["char"]
		num = item["num"]
		print(f"The '{char}' character was found {num} times")
print("--- End Report ---")
