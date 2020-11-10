# 노드와 노드 그룹을 관리하는 클래스 정의

class Node :
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

class NodeMgmt:
    # NodeMgmt 가 만들어질때 head의 정보까지 한번에 만들어진다 >> 초기 노드가 하나 존재하게됨
    def __init__(self, data) :
        self.head = Node(data)

    def add(self, data) :
        if self.head == '':
            self.head = Node(data)
        else :
            node = self.head
            while node.next :
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedlist1= NodeMgmt(0)
linkedlist1.desc()
print()
for index in range(1,10):
    linkedlist1.add(index)

linkedlist1.desc()