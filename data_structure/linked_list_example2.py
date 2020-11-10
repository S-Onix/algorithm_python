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

    # 1. head 삭제
    # 2. 마지막 노드 삭제
    #       마지막 노드 삭제 이후 그 이전 Node의 next 값을 None으로 변환
    # 3. 중간 노드 삭제
    def delete(self, data) :
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다')
            return
        
        if self.head.data == data :
            temp = self.head
            self.head = self.head.next
            del temp
        else :
            node = self.head
            while node.next :
                if node.next.data == data :
                    # 이전 노드, 이후 노드를 연결해줘야함 + 중간 노드 삭제
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else :
                    node = node.next


linkedlist1= NodeMgmt(0)
linkedlist1.desc()
print()
for index in range(1,10):
    linkedlist1.add(index)

linkedlist1.desc()

linkedlist1.delete(4)
linkedlist1.delete(9)
linkedlist1.delete(10)
print()
linkedlist1.desc()
