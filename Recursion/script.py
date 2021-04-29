
def findTrio(arr, n, sumValue):

    result = False

    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == sumValue):
                    print("The trio which contains the given sum is",
                          {arr[i], arr[j], arr[k]})
                    result = True

    if (result == False):
        print("Trio does not exist")


arr = [3, 7, 4, 0, 9, 5, 1, 2]
n = len(arr)
sumValue = 7
findTrio(arr, n, sumValue)
