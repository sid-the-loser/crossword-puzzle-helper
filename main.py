import json

dictionary = json.loads(open("dictionary.json").read().lower())

while True:

    word_to_browse = input("Enter the word to browse (ex: 'lo#e' where '#' is unknown): ").lower()

    f = open("answers.txt", "w")

    known_positions = []

    for i in range(len(word_to_browse)):
        if word_to_browse[i] != "#":
            known_positions.append(i)

    for word in dictionary:
        if len(word) == len(word_to_browse):
            for pos in known_positions:
                if word[pos] != word_to_browse[pos]:
                    break
            else:
                f.write(f"{word}: {dictionary[word]}\n\n\t***\n")

    f.close()