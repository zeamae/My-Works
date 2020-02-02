def mergeSortedArrays(array1, array2):
    i=0
    j=0
    len1 = len(array1)
    len2 = len(array2)

    array = []

    while((i<len1) and (j<len2)):
        if(array1[i] < array2[j]):
            array.append(array1[i])
            i = i + 1
        else:
            array.append(array2[j])
            j = j + 1
    while(i < len1):
        array.append(array1[i])
        i = i + 1

    while(j < len2):
        array.append(array2[j])
        j = j + 1
    return array


array1 = [1,4,5,7]
array2 = [2,3,6,8]
array = mergeSortedArrays(array1,array2)
print(array)