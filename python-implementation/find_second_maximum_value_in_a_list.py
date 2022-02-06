def find_second_maximum(lst):
    # Write your code here
    import sys
    arr = lst
    max, second_max = arr[0], -sys.maxsize - 1
    for i in range(0, len(lst)):
        if arr[i] > max:
            second_max = max
            max = arr[i]
        elif arr[i] < max and arr[i] > second_max:
            second_max = arr[i]

    return second_max
