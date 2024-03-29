![IMG_7513](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/4e96d942-791e-4d88-be04-32b8ac37c6c7)
![IMG_7514](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/d90bbf65-b28d-4f1c-b970-686e678720ec)

### Algorithm Summary
#### Steps:
1. **Sort jobs by profit**: Sort the `jobs` list in descending order based on the profit of each job.
2. **Determine maximum deadline**: Find the maximum deadline among all jobs.
3. **Initialize variables**: 
    - `max_deadline` to store the maximum deadline.
    - `job_count` to count the number of jobs scheduled.
    - `profit` to accumulate the total profit earned.
    - `deadline_arr` as a boolean array to mark whether a deadline is occupied or not.
4. **Iterate over jobs**: For each job in the sorted list:
    - Update `max_deadline`.
5. **Initialize `deadline_arr`**: Create a boolean array `deadline_arr` of size `max_deadline + 1`, initialized with `False`.
6. **Schedule jobs**: Iterate over the jobs again:
    - For each job, iterate backward from its deadline to 1:
        - If the deadline slot is empty (`False`), mark it as occupied (`True`), increase `job_count`, add the profit of the job to the total `profit`, and break the loop.
7. **Return result**: Return `[job_count, profit]`.

