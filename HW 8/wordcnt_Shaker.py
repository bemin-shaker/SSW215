def word_count():
    with open('HW 8/alice.txt') as file_object:
        contents = file_object.read()
        words = contents.split()
    return len(words)


print("The file alice.txt has about", word_count(), "words")
