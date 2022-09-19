class Node:
    def __init__(self, key=None):
        self.key = key 
        self.next = self # 자기자신을 가르킨다.
        self.prev = self # 자기자신을 가르킨다.

    def __str__(self):
        return str(self.key)

    
class Doubly_Linked_List:
    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node.next != self.head:
            yield node.key
            node = node.next
        return StopIteration 

    def splice(self, a, b, x): 
        # a, b, x 는 모두 Node이다.
        # 조건1
        # a의 next를 따라가다보면 b가 있다.
        # a,b 가 모두 a,a일 수도 있다.

        # 조건2
        # a와 b사이에 head(dummy node)가 있으면 안된다.
        # 원형으로 연결되어있기 때문에 next를 해서 a-b사이에 dummy가 올수도 있기 때문에 이점을 주의하자
        
        # 조건3
        # a와 b사이에 x가 있으면 안된다.

        # cut하기
        a.prev.next = b.next
        b.next.prev = a.prev
        
        # paste하기
        x.next = a
        a.prev = x
        b.next = x.next
        x.next.prev = b


    # 이동연산
    # 노드 a를 노드 x 다음으로 이동시킨다.
    def move_After(self, a, x):
        self.splice(a, a, x)

    # 노드 a를 노드 x 앞으로 이동시킨다.
    # x의 앞에 해당하므로 splice에서는 x.prev에 해당한다.
    def move_Before(self, a, x):
        self.splice(a, a, x.prev)

    # 삽입연산 
    # 이동연산을 다시 불러서 활용한다.
    def insert_After(self, x, key):
        self.move_After(Node(key), x)
        self.size += 1

    def insert_Before(self, x, key):
        self.move_Before(Node(key), x)
        self.size += 1

    def push_Front(self, key):
        self.insert_After(self.head, key)
        self.size += 1

    def push_Back(self, key):
        self.insert_Before(self.head, key) 
        self.size += 1

    # 탐색연산
    # 헤드부터 차례대로 비교하면서 링크를 따라간다.
    def search(self, key):
        node = self.head
        while node.next != self.head:
            if node.key == key:
                return node
            node = node.next
        return None

    
    def remove(self, x):
        x = self.search(x)
        if x == None or x == self.head:
            return None
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
        del x

    def pop_Front(self):
        if self.size == 0:
            return None
        self.remove(self.head.next)
    
    def pop_Back(self):
        if self.size == 0:
            return None
        self.remove(self.head.prev)

test = Doubly_Linked_List()
