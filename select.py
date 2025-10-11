def partition(arr, left, right):
    pivot = arr[right]  # Choose last element as pivot
    i = left - 1        # Index for smaller element
    for j in range(left, right):
        if arr[j] <= pivot:   # If current element <= pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Place pivot in correct position
    return i + 1  # Return pivot index


def quickselect(arr, left, right, k):
    # k is 1-based (k = 1 means smallest element)
    if left <= right:
        pivot_index = partition(arr, left, right)
        rank = pivot_index - left + 1  # Position of pivot in the current subarray

        if k == rank:
            return arr[pivot_index]
        elif k < rank:
            return quickselect(arr, left, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, right, k - rank)
    
    # If k is out of range
    raise IndexError("k is out of bounds")


# Example test
A = [8, 4, 1, 5, 9, 2]
k = 3
print(f"The {k}rd smallest element is:", quickselect(A, 0, len(A) - 1, k))
