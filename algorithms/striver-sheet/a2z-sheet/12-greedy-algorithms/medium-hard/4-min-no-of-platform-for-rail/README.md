![IMG_7511](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/d68aef2b-b513-4e57-bede-8fa256fde535)

Algorithm Summary: Calculate Minimum Platforms

Description:
This algorithm calculates the minimum number of platforms required at a train station given the arrival and departure times of trains.

Inputs:
- `at`: List of arrival times of trains.
- `dt`: List of departure times of trains.
- `n`: Number of trains.

Output:
- Prints the minimum number of platforms required at the station.

Steps:
1. Sort the arrival times (`at`) and departure times (`dt`) lists.
2. Initialize variables: `cur_plat` and `max_plat` as 0, `arr_index` and `dep_index` as 0.
3. Iterate through the arrival times list:
   a. While the arrival time at `arr_index` is greater than the departure time at `dep_index`, decrease `cur_plat` and increment `dep_index`.
   b. Increment `cur_plat` by 1.
   c. Update `max_plat` to the maximum of `cur_plat` and `max_plat`.
   d. Move to the next arrival time by incrementing `arr_index`.
4. Print the value of `max_plat`, which represents the minimum number of platforms required.

Example Usage:
```python
arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]
calculateMinPatforms(arrival_times, departure_times, 6)
# Output: 3
