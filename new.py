def missingNumbers(array):
    newList = []
    for i in range(min(array), max(array)):
        if i not in array and i not in newList and i > 0:newList.append(i)
        elif i + 1 not in array and i not in newList and i > 0:newList.append(i + 1)
    return newList if newList != [] else "There's no missing number on the array"
print(missingNumbers([1,2,3,4,5,-8]))