# 링크드리스트(구조)
# 연결 리스트라고 말함
# 구조를 구현하기 위해서는 클래스를 하나 정의해서 만들어야함
# 기본적인 구조는 데이터를 담고 있는 공간과 연결시켜줄 공간을 가지고 있어야한다.
# 일반적으로 노드라고 이야기하며
# 노드는 데이터값, 포인터로 구성된다.
# 포인터란 각 노드 안에서 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간이라고 생각하면 된다.
# 파이썬에서는 클래스의 메소드 안에 첫번째 인자는 self 가 존재하며 이 self는 자바에서의 this와 역할이 동일하다.


# 링크드리스트의 장점 : 배열과 비교해 봤을 때 데이터 공간을 미리 할당하지 않아도 됨
# 링크드리스트의 단점 : 별도의 데이터 공간이 필요하므로 저장공간의 효율이 좋지 않다. (데이터, 포인터)
#                     연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다 (Node를 건너서 찾아야하기 때문에 (인덱스로 찾는것이 아님))
#                     중간 데이터 삭제시, 앞뒤 데이터 연결을 재구성해야하는 부가적인 작업이 필요하다.  

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

node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else :
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next