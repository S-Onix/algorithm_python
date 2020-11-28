# 힙 자료구조
# 힙은 트리를 기반으로 특정 목적에 맞춰 변형된 자료구조이다.
# 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리이다.
# 완전 이진 트리란 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리를 의미한다.

# 힙은 최대값을 구하기 위한 구조와 최소값을 구하기 위한 구조로 분류할수 있다.
# 최대힙의 경우에는 각 노드의 값은 해당 노드의 자식 노드가 가진 값 보다 크거나 같다 >> 부모는 무조건 자식보다 크다.
# 최소힙의 경우에는 최대힙과 반대로 각 노드의 값은 해당 노드의 자식 노드가 가진 값 보다 작거나 같다 >> 부모는 무조건 자식보다 작다.

# 완전이진트리의 구조를 지니기 때문에 왼쪽 노드부터 채워간다.

# 힙은 최대값, 최소값을 빠르게 찾기위함
# 이진탐색트리는 탐색을 위한 구조
# 동일하게 이진 트리이지만 역할이 다르다.

# List 형식으로 데이터를 담아 놓는다
# 부모노드를 찾는 법은 왼쪽 자식노드의 위치 * 2
# 자식노드를 찾는 법은 부모노드의 위치 *2 / 부모노드의 위치 * 2 + 1 
# 위의 세가지 식을 이용하면 데이터의 위치를 찾을 수 있을 뿐더러 빠른 비교후 데이터 입력 삭제가 가능하다.

class Heap :
    def __init__(self, data) :
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx) :
        # 바꿔줘야 하면 return True

        # 루트노드의 여부 확인
        if inserted_idx <= 1 :
            return False
        # 부모노드와 값 비교
        if self.heap_array[inserted_idx] > self.heap_array[inserted_idx // 2] :
            return True
        else :
            return False

    def insert(self, data) :
        # root 노드가 없을 경우
        if len(self.heap_array) == 0 :
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        # 이진트리의 형식에 맞게 데이터를 세팅함
        self.heap_array.append(data)

        # 들어온 데이터와 부모 노드의 데이터를 비교 후 swap 해주는 작업이 필요하다.
        # 현제 list의 길이는 0번쨰에 임의로 추가해놓았기 마지막 노드의 위치는 len(list) -1 이다.
        inserted_idx = len(self.heap_array) - 1
        # swap 여부를 확인하는 메소드
        while self.move_up(inserted_idx) :
            # 부모와 자식 노드를 swap한다.
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx],self.heap_array[parent_idx]  = self.heap_array[parent_idx],self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, poped_idx) :
        left_child_poped_idx = poped_idx * 2 
        right_child_poped_idx = poped_idx * 2 + 1

        # 왼쪽 자식 노드가 존재하지 않을 경우
        if len(self.heap_array) <= left_child_poped_idx :
            return False
        # 왼쪽 자식 노드만 존재할 경우
        elif len(self.heap_array) <= right_child_poped_idx :
            if self.heap_array[left_child_poped_idx] > self.heap_array[poped_idx] :
                return True
            else :
                return False
        # 왼쪽, 오른쪽 자식 노드가 모두 존재할 경우
        else :
            # 왼쪽과 오른쪽 노드의 크기 비교
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx] :
                if self.heap_array[left_child_poped_idx] > self.heap_array[poped_idx] :
                    return True
                else : 
                    return False
            else :
                if self.heap_array[right_child_poped_idx] > self.heap_array[poped_idx] :
                    return True
                else : 
                    return False


    def pop(self) :
        if len(self.heap_array) <= 1 :
            return None
        
        # 최대값 추출
        returnd_data = self.heap_array[1]

        # 가장 마지막 위치의 노드를 최상위로 위치한다.
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        
        # 최대값 추출 이후 다시 재정렬 과정이 필요하다 (최대 힙이기 때문에 루트노드는 가장 큰값이 되어야함)
        poped_idx = 1
        
        # 재정렬을 위한 로직 수행
        while self.move_down(poped_idx) :
            left_child_poped_idx = poped_idx * 2 
            right_child_poped_idx = poped_idx * 2 + 1
            # 왼쪽 노드만 있는 경우
            if right_child_poped_idx >= len(self.heap_array) :
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx] :
                    self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx] , self.heap_array[poped_idx]
                    poped_idx = left_child_poped_idx
            # 왼쪽, 오른쪽 노드가 둘다 존재하는 경우
            else :
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx] :
                    if self.heap_array[left_child_poped_idx] > self.heap_array[poped_idx] :
                        self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx] , self.heap_array[poped_idx]
                        poped_idx = left_child_poped_idx
                else :
                    if self.heap_array[right_child_poped_idx] > self.heap_array[poped_idx] :
                        self.heap_array[poped_idx], self.heap_array[right_child_poped_idx] = self.heap_array[right_child_poped_idx] , self.heap_array[poped_idx]
                        poped_idx = right_child_poped_idx
        
        return returnd_data
            


 
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.insert(30)
heap.insert(11)
print('pop data : ', heap.pop())
print('pop data : ', heap.pop())
print(heap.heap_array)

