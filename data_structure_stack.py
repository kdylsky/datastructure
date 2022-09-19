class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is Empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")
        
    def __len__(self):
        return len(self.items)
            

lst = ["(", ")", "(", ")", "(", "(", ")", ")",")","("]

def is_couple(lst):
    try:
        stack = Stack()
    
        for i in range(len(lst)):
            
            if lst[i] == "(":
                stack.push(lst[i])
            elif lst[i] == ")":
                stack.pop()
            else:
                continue
        
        if len(stack) > 0:
            return False
        
        else:
            return True
    except:
        return False

# a = is_couple(lst)
# print(a)



# input = input().split()
input = "1*2+(3-2)*4"
token_list = [i for i in input]
stack = Stack()
result_lst = []

def infix_to_postfix(input):
    for token in token_list:
        if token == "(":

            stack.push(token)
        
        elif token == ")":
            for i in range(len(stack)):
                if stack.top() == "(":
                    stack.pop()
                    break
                else:
                    result_lst.append(stack.pop())
        
        elif token == "+" or token =="-":
            if len(stack) == 0:
                stack.push(token)
            else:
                for i in range(len(stack)):
                    if stack.top() == "*" or stack.top() == "/":
                        result_lst.append(stack.pop())              
                    
                    elif stack.top() == "+" or stack.top() == "-":
                        result_lst.append(stack.pop())
                    
                    elif stack.top() == "(":
                        break
                stack.push(token)
        
        elif token == "*" or token == "/":
            if len(stack) == 0:
                stack.push(token)
            else:
                for i in range(len(stack)):
                    if stack.top() == "+" or stack.top() == "-" :
                        continue
                    elif stack.top() == "*" or stack.top() == "/":
                        result_lst.append(stack.pop())
                    elif stack.top() =="(":
                        break
                stack.push(token)
        else:
            result_lst.append(token)
        
    if len(stack) > 0:
        for i in range(len(stack)):
            result_lst.append(stack.pop())
    
    return result_lst

token_list = infix_to_postfix(input)
print(token_list)

import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv } 


stack = Stack()
for token in token_list:
    if token in ["+","-","*","/"]:
        a = int(stack.pop())
        b = int(stack.pop())
        result = ops[token](b,a)     
        stack.push(result)
    else:
        stack.push(token)

print(stack.pop())










