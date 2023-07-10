# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest_in_array(arr, n):
    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
