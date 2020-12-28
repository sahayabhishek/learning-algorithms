# Question
#
# The input file 'IntegerArray.txt' contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some
# order, with no integer repeated.
#
# The task is to compute the number of inversions in the file given, where the i^{th} row of the file indicates
# the i^{th} entry of an array.
#

# load_arr reads data in a file and loads it into an array
def load_arr(file_name):
    arr = []
    with open(file_name) as fp:
        lines = fp.readlines()
        for line in lines:
            arr.append(int(line.strip()))
    return arr


# sort_and_count_split_inversions performs merge logic for the two sorted arrays and counts the inversions between
# those 2 arrays.
def sort_and_count_split_inversions(left_arr, right_arr):
    left_arr_len = len(left_arr)
    right_arr_len = len(right_arr)
    sorted_arr = [None] * (left_arr_len + right_arr_len)

    inv_count = 0

    i = j = k = 0

    while i < left_arr_len and j < right_arr_len:
        if left_arr[i] <= right_arr[j]:
            sorted_arr[k] = left_arr[i]
            i += 1
        else:
            inv_count += (left_arr_len - i)
            sorted_arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < left_arr_len:
        sorted_arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < right_arr_len:
        sorted_arr[k] = right_arr[j]
        j += 1
        k += 1

    return inv_count, sorted_arr


# sort_and_count_inversions method counts the number of inversions in the array and also returns a sorted array.
# Array is sorted using merge sort algorithm. Time complexity of merge sort is O(n*log(n)).
def sort_and_count_inversions(arr):
    length_arr = len(arr)
    # Base case for recursion to exit
    if length_arr == 1:
        return 0, arr
    else:
        # Split the array in two and then recursively sort and count inversions in each half.
        # Then count the split inversions (i.e. inversions between the two halves using the sorted array).
        # Sum total of these 3 counts of inversion gives the number of inversions in the array.
        middle_index = length_arr // 2
        left_arr = arr[:middle_index]
        right_arr = arr[middle_index:]
        left_inv_count, left_arr_sorted = sort_and_count_inversions(left_arr)
        right_inv_count, right_arr_sorted = sort_and_count_inversions(right_arr)
        split_inv_count, arr_sorted = sort_and_count_split_inversions(left_arr_sorted, right_arr_sorted)
        return left_inv_count + right_inv_count + split_inv_count, arr_sorted


if __name__ == '__main__':
    arr = load_arr('IntegerArray.txt')
    cnt, sorted_arr = sort_and_count_inversions(arr)
    print cnt
