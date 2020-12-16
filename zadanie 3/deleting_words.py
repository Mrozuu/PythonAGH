with open('tekst.txt', 'r', encoding='UTF8') as file:
    text_input = file.read()

delete_words = ["się", "i", "oraz", "nigdy", "dlaczego"]
text_output = ""

split_lines = text_input.splitlines()
for line in split_lines:
    split_words = line.split()
    words_output = [word for word in split_words if word.lower() not in delete_words]
    text_output += ' '.join(words_output)
    text_output += '\n'

print(text_output)
