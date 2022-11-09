from Stack import MyStack
import re

def evaluate_post_fix(exp):
    # Write your code here
    exp = exp.replace(" ","")
    stack = MyStack()
    result = None
    for item in exp:
        if item.isdigit():
            stack.push(item)
        else:
            second_num = int(stack.pop())
            first_num = int(stack.pop())
            if item == "+":
                stack.push(first_num + second_num)
            elif item == "-":
                stack.push(first_num - second_num)
            elif item == "*":
                stack.push(first_num * second_num)
            elif item == "/":
                stack.push(first_num / second_num)
        
    
    print(stack.peek())
    return stack.pop()


evaluate_post_fix("921 * - 8 - 4 +")


"""
Approach 1 
def evaluate_post_fix(exp):
    # Write your code here
    exp = exp.replace(" ","")
    stack = MyStack()
    result = None
    for item in exp:
        if item == "+" or item == "-" or item == "*" or item == "/":
            second_num = int(stack.pop())
            first_num = int(stack.pop())
            if item == "+":
                stack.push(first_num, item,second_num)
            elif item == "-":
                stack.push(first_num - second_num)
            elif item == "*":
                stack.push(first_num * second_num)
            elif item == "/":
                stack.push(first_num / second_num)
        else:
            stack.push(item)
    
    print(stack.peek())
    return stack.pop()
"""