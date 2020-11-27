# 트리 : Node 와 Branch를 이루어진 데이터 구조
# Node간 Branch로 연결되어 있음
# 가장 상단에 있는 노드를 Root라고 불림
# 2진 트리 : 노드의 최대 Branch가 2인 트리
# 2진 탐색 트리 : 이진 트리에서 추가적인 조건이 있음 >> 왼쪽 노드는 해당 노드보다 적은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있어야함.
# 장점 : 탐색 속도를 개선할 수 있다.
# 단점 : 구현하기 쉽지 않음
import random


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
        while self.current_node :
            if self.current_node.value == value :
                return True
            else :
                # 왼쪽으로 탐색을 할지 오른쪽으로 탐색할지 결정 위한 분기 구문
                if self.current_node.value > value : 
                    self.current_node = self.current_node.left
                else :
                    self.current_node = self.current_node.right
        return False
    # 노드의 존재유무를 찾아 삭제한다. >> 부모와 자식을 연결해주는 작업이 필요하다.
    def delete(self, value) :
        searched = False
        self.current_node = self.head
        self.parent_node = self.head

        # 삭제할 노드가 있는지 검사하는 구문
        while self.current_node :
            if self.current_node.value == value :
                searched = True
                break
            elif self.current_node.value > value : 
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            else :
                self.parent_node = self.current_node
                self.current_node = self.current_node.right

        # 삭제할 노드가 없다면 리턴
        if searched == False :
            return False
        
        # 삭제할 노드가 Leaf Node(가장 Depth가 큰)일 경우
        if self.current_node.left == None and self.current_node.right == None :
            if value < self.parent_node.value :
                self.parent_node.left = None
            else :
                self.parent_node.right = None
            del self.current_node
        
        # 삭제할 노드의 Child Node가 하나일때
        # left에 존재할 경우
        if self.current_node.left != None and self.current_node.right == None :
            # 왼쪽에 존재할 경우 >> current의 왼쪽의 노드와 부모의 노드의 왼쪽과 연결되어야 한다.
            if value < self.parent_node.value :
                self.parent_node.left = self.current_node.left
            else :
                self.parent_node.right = self.current_node.left
            del self.current_node
        # right에 존재할 경우
        elif self.current_node.left == None and self.current_node.right != None :
            if value < self.parent_node.value :
                self.parent_node.left = self.current_node.right
            else :
                self.parent_node.right = self.current_node.right
            del self.current_node
        
        # 삭제할 노드의 Child Node가 두개일때
        # 삭제할 노드가 parent의 왼쪽에 있을 경우
        #   삭제할 노드의 오른쪽 자식 중 가장 작은 값을 삭제할 위치로 올리는 경우
        #       가장 작은 노드의 자식 노드가 존재할 경우
        #       가장 작은 노드의 자식 노드가 존재하지 않을 경우
        #   삭제할 노드의 왼쪽 자식 중 가장 큰 값을 삭제할 위치로 올리는 경우
        #       가장 큰 노드의 자식 노드가 존재할 경우
        #       가장 큰 노드의 자식 노드가 존재하지 않을 경우
        # 삭제할 노드가 parent의 오른쪽에 있을 경우
        if self.current_node.left != None and self.current_node.right != None :
            # 삭제할 노드의 값(위치)이 부모의 노드보다 작을때 >> 왼쪽에 존재할 경우
            if value < self.parent_node.value :
                # 삭제할 노드는 current_node 이다.
                # 변경될 노드와 변결될 노드의 부모의 초기값은 삭제될 노드의 오른쪽 노드이다.
                self.change_node_parent = self.current_node.right
                self.change_node = self.current_node.right
                # 최소 값을 가지는 노드를 찾기 위한 순회 과정
                while self.change_node.left :
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # 최소 값을 가지는 노드가 자식 노드를 가지고 있는 경우 (오른쪽 노드만 가지고 있음)
                if self.change_node.right :
                    # 변경될 노드의 부모 노드와 변경될 노드의 자식 노드를 연결해줘야한다.
                    self.change_node_parent.left = self.change_node.right
                else : 
                    # 변경될 부모 노드의 왼쪽을 끊어준다.(순환구조(Cycle) 형성이 되면 안되기 때문에)
                    self.change_node_parent.left = None
                # 삭제될 노드의 왼쪽을 변경될 노드로 연결해준다.
                self.parent_node.left = self.change_node
                # 삭제될 노드의 오른쪽 노드와 왼쪽노드를 변경될 노드의 왼쪽 노드와 오른쪽 노드로 변경해준다.
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
                
            else :
                self.change_node_parent = self.current_node.right
                self.change_node = self.current_node.right
                while self.change_node.left :
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right :
                    self.change_node_parent.left = self.change_node.right
                else :
                    self.change_node_parent.left = None
                self.parent_node.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
            
            # 노드를 삭제한다.
            del self.current_node
        return True

head = Node(1)
BST = NodeMgt(head)
BST.insert(3)
print(BST.search(3))
print(BST.search(2))

# 1-1000 숫자 중 임의로 100개 추출, 이진 탐색 트리에서 입력, 검색, 삭제
bst_nums = set()
while len(bst_nums) != 100 :
    bst_nums.add(random.randint(0,999))

print(bst_nums)