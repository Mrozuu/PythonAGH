with open('tekst.txt', 'r', encoding='UTF8') as file:
    text_input = file.read()

to_change = ["i", "oraz", "nigdy", "dlaczego"]
change_with = ["oraz", "i", "prawie nigdy", "czemu"]

text_output = ""
split_lines = text_input.splitlines()

for line in split_lines:
    split_words = line.split()
    words_output = []
    for word in split_words:
        if word not in to_change:
            words_output.append(word)
        else:
            words_output.append(change_with[to_change.index(word)])
    text_output += ' '.join(words_output)
    text_output += '\n'

print(text_output)
