
list = [1, 2, 5, 9, 16, 3, 5, 10, 9, 7]


def square(list):
    newList = []
    for i in list:
        newList.append(i**2)
    print(newList)


square(list)
