class Node:
    def __init__(self,key):
        self.key    = key
        self.next   = None
    
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def pushfront(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:     
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        
    def pushback(self, key):
        new_tail = Node(key)
        if self.size == 0:
            self.head = new_tail
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_tail
        self.size += 1
        
    def popfront(self):
        if self.size == 0:
            return None
        else:
            curr_head = self.head
            return_value = curr_head.key

            self.head = curr_head.next
            self.size -= 1

            del curr_head

            return return_value

    def popback(self):
        if self.size == 0:
            return None
        else:
            pre_tail, curr_tail = None, self.head
            while curr_tail.next != None:
                pre_tail = curr_tail
                curr_tail = curr_tail.next
            
            if self.size == 1:
                self.head = None
            
            else:
                pre_tail.next = curr_tail.next
            
            return_value = curr_tail.key
            del curr_tail
            self.size -= 1
            
            return return_value

    def search(self, key):
        search_node = self.head
        while search_node != None:
            if search_node.key == key:
                return search_node
            search_node = search_node.next
        return None

    def __iter__(self):
        node = self.head
        while node != None:
            yield node.key
            node = node.next
        return StopIteration    
    

lst = SinglyLinkedList()
lst.pushfront(10)
lst.pushfront(20)
lst.pushfront(30)
lst.pushfront(40)
lst.pushfront(50)
lst.pushfront(60)
lst.pushfront(70)

for i in lst:
    print(i.key)