# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index


def selectionsort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
