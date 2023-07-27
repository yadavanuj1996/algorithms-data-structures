from interval import Interval

"""
Time Complexity: O(n + m)
Space Complexity: O(n)
"""
def intervals_intersection(interval_list_a, interval_list_b):
    first,second = 0, 0
    start, end = 0, 1
    result = []
    while first < len(interval_list_a) and second < len(interval_list_b):
        if are_intervals_overlapping(interval_list_a[first], interval_list_b[second]):
            result.append(Interval(
                    max(interval_list_a[first].start, interval_list_b[second].start),
                    min(interval_list_a[first].end, interval_list_b[second].end)
            ))
        
        if interval_list_a[first].end < interval_list_b[second].end:
            first += 1
        else:
            second += 1
    
    return result

def are_intervals_overlapping(arr1, arr2):
    if arr2.start <= arr1.start <= arr2.end or arr2.start <= arr1.end <= arr2.end or arr1.start <= arr2.start <= arr1.end or arr1.start <= arr2.end <= arr1.end:
        return True

    return False

def main():
    #interval_list_a = [Interval(2,6), Interval(7,9), Interval(10,13), Interval(14,19), Interval(20,24)]
    #interval_list_b = [Interval(1,4), Interval(6,8), Interval(15,18)]
    interval_list_a = [Interval(1, 29)]
    interval_list_b = [Interval(1,5), Interval(6,10), Interval(11,14), Interval(15,18), Interval(19,20)]
    
    print(intervals_intersection(interval_list_a, interval_list_b))

if __name__ == "__main__":
    main()