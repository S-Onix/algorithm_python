# Doublc Linked List
# 양방향 

class Node :
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class NodeMgmt :
    # 처음과 끝을 동시에 지정함
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert(self, data):
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head
        else :
            node = self.head
            while node.next :
                node = node.next
            # 앞뒤로 연결해주는 코드
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node
            self.tail = new_node


    def desc(self):
        node = self.head 
        while node :
            print(node.data)
            node = node.next

    def search_from_head(self, data) :
        if self.head == None :
            return False

        node = self.head
        while node :
            if node.data == data :
                return node
            else :
                node = node.next
        return False

    def search_from_tail(self, data) :
        if self.head == None :
            return False
        
        node = self.tail
        while node :
            if node.data == data :
                return node
            else:
                node = node.prev
        return False
        
    def insert_before(self, data, before_data) :
        if self.head == None :
            self.head = Node(data)
            return True
        else :
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None :
                    return False
            new_node = Node(data)
            before_new = node.prev
            before_new.next = new_node
            new_node.prev = before_new
            node.prev = new_node
            new_node.next = node



double_linked_list = NodeMgmt(0) 
for index in range(1,10) :
    double_linked_list.insert(index)

double_linked_list.desc()

search_node = double_linked_list.search_from_head(3)
search_node2 = double_linked_list.search_from_head(10)

print(search_node.data)
print(search_node2)

    