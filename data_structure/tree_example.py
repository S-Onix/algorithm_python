# 트리 : Node 와 Branch를 이루어진 데이터 구조
# Node간 Branch로 연결되어 있음
# 가장 상단에 있는 노드를 Root라고 불림
# 2진 트리 : 노드의 최대 Branch가 2인 트리
# 2진 탐색 트리 : 이진 트리에서 추가적인 조건이 있음 >> 왼쪽 노드는 해당 노드보다 적은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있어야함.
# 장점 : 탐색 속도를 개선할 수 있다.
# 단점 : 구현하기 쉽지 않음

#노드 구현
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None



class NodeMgt :
    # 클래스 생성시 Head를 지정하여 넣어준다.
    def __init__(self, head) :
        self.head = head 

    def insert(self, value) :
        # 시작 지점은 헤드(root)이다.
        self.current_node = self.head
        while True :
            # 넣는 값이 더 작을 경우 기준 노드의 왼쪽으로 진행되어야한다.
            if value < self.current_node.value :
                if self.current_node.left != None :
                    self.current_node = self.current_node.left
                else :
                    self.current_node.left = Node(value)
                    break
            # 넣는 값이 더 클 경우 기준 노드의 오른쪽으로 진행되어야한다.
            else :
                if self.current_node.right != None :
                    self.current_node = self.current_node.right
                else :
                    self.current_node.right = Node(value)
                    break
    # 해당 노드의 존재여부에 대해서 알기 위한 메소드    
    def search(self, value) :
        self.current_node = self.head
        while(self.current_node) :
            if self.current_node.value == value :
                return True
            else :
                # 왼쪽으로 탐색을 할지 오른쪽으로 탐색할지 결정 위한 분기 구문
                if self.current_node.value > value : 
                    self.current_node = self.current_node.left
                else :
                    self.current_node = self.current_node.right
        return False

        

head = Node(1)
BST = NodeMgt(head)
BST.insert(3)
print(BST.search(3))
print(BST.search(2))