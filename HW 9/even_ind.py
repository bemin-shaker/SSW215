def even_values_index(str):
    result = ""
    for i in range(len(str)):
        if i % 2 != 0:
            result = result + str[i]
    return result


print(even_values_index('Individual software engineering'))
