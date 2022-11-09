from Stack import MyStack

def next_greater_element(lst):
    result =  [-1 for x in lst]
    stack = MyStack()
    for iteration in range(len(lst)):
        if not stack.is_empty():
            while not stack.is_empty() and lst[stack.peek()] < lst[iteration]:
                result[stack.pop()] = lst[iteration]
            stack.push(iteration)
        else:
            stack.push(iteration)

    print(result)
    return result

next_greater_element([4,1,3])