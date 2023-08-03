def least_time(tasks, n):
    idle_time = 0
    current = {}

    for task in tasks:
        current[task] = current.get(task, 0) + 1
    
    current = dict(sorted(current.items(), key=lambda x: x[1], reverse=True))
    max_freq_key = max(current, key=lambda x: current[x])
    max_freq = current[max_freq_key]
    del current[max_freq_key]
    # Max idle time 
    idle_time = (max_freq - 1) * n
    # Loop over each item except max element (as it is removed) and calculate idle_time
    for item in current:
        if idle_time <= 0:
            idle_time = 0
            break
        
        current_freq = current[item]
        idle_time = idle_time - min(max_freq-1, current_freq)
        

    total_tasks = len(tasks)
    return total_tasks + idle_time


def main():
    #tasks = ["A","B","A","A", "B", "C"]
    #n = 3
    tasks = ["A", "B", "C", "O", "Q", "C", "Z", "O", "X", "C", "W", "Q", "Z", "B", "M", "N", "R", "L", "C", "J"] 
    n = 10
    #tasks = ["A", "A", "A", "B", "B", "C", "C"]
    #n = 1
    print(least_time(tasks, n))

if __name__ == "__main__":
    main()
