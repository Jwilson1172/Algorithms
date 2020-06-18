'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# not really sure why this isn't passing the test.
def single_number(arr):
    # Your code here
    cursor = 0
    while cursor != len(arr):
        # check if the current element is the same as the next element if so
        # jump to the next tuple
        if arr[cursor] == arr[cursor + 1]:
            cursor += 2
            print("found 2 {} skipping this number".format(arr[cursor - 1]))
        # check if the current and next are diffrent
        elif arr[cursor] != arr[cursor + 1]:
            return arr[cursor]
        else:
            print("an unknown case occured please refactor code.")
            return -1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
