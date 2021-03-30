sentence = "Mango banana apple pear Banana grapes strawberry Apple pear mango banana Kiwi apple mango strawberry"

list1 = []


def char_index(text):
    startingPos = 0

    position = text.find("r", startingPos)
    startingPos = position
    list1.append(position)
    while position > -1:
        startingPos = position + 1
        position = text.find("r", startingPos)
        list1.append(position)

    list1.remove(-1)

    return list1


output = char_index(sentence)

print("The index values of each occurrence of character ‘r’in the string are: ", output)
