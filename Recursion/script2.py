
def printArray(arr, n):

    for i in range(0, n):
        print(arr[i], end=" ")

    print("")


def generateSequence(x, arr, current_sum, current_index):
    if (current_sum == x):
        printArray(arr, current_index)
        return
    num = 1

    while (num <= x - current_sum and
           (current_index == 0 or
            num <= arr[current_index - 1])):
        arr[current_index] = num
        generateSequence(x, arr, current_sum + num, current_index + 1)
        num += 1


def generate(x):
    arr = [0] * x
    generateSequence(x, arr, 0, 0)


x = 4
generate(x)
