class Queue:
    def __init__(self):
        self.items = []
        self.front_idx = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_idx == len(self.items):
            return None
        else:
            x = self.items[self.front_idx]
            self.front_idx += 1
            return x

def josephus_problem(n,k):
    queue = Queue()
    lst   = []
    for i in range(1, n+1):
        queue.enqueue(i)

    
    while len(lst) != n-1:
        
        for i in range(k-1):
            queue.enqueue(queue.dequeue())
        lst.append(queue.dequeue())

        
    return queue.dequeue()
    
n = 6
k = 2
result = josephus_problem(n, k)
print(result)

from collections import deque

a = deque([1,2,3])

a.append(4)
a.appendleft(5)

a.pop()
a.popleft()



