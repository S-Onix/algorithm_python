# 링크드리스트(구조)
# 연결 리스트라고 말함
# 구조를 구현하기 위해서는 클래스를 하나 정의해서 만들어야함
# 기본적인 구조는 데이터를 담고 있는 공간과 연결시켜줄 공간을 가지고 있어야한다.
# 일반적으로 노드라고 이야기하며
# 노드는 데이터값, 포인터로 구성된다.
# 포인터란 각 노드 안에서 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간이라고 생각하면 된다.
# 파이썬에서는 클래스의 메소드 안에 첫번째 인자는 self 가 존재하며 이 self는 자바에서의 this와 역할이 동일하다.


class Node:
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

head = Node(1)

def add(data):
    node = head
    # node.next 가 존재할시에 아래 while문을 진행한다
    while node.next :
        node = node.next
    # while문을 빠져나왔다는 것은 마지막 노드라는 의미이며 마지막 노드의 next 에 새로운 Node를 추가해준다.
    node.next = Node(data)

for index in range(2,10):
    add(index)

def print_node():
    node = head
    while node.next:
        print(node.data)
        node = node.next
    print(node.data)

print_node()