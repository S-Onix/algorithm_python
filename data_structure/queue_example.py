import queue
# queue 라이브러리가 존재하며
# 1. Queue() : 가장 일반적인 큐 자료 구조
# 2. LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조)
# 3. PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
# 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 큐가 많이 사용됨 (운영체제)

# 일반적인 큐 구현
data_queue = queue.Queue()
data_queue.put(10)
data_queue.put('Test')
print(data_queue.qsize())

print(data_queue.get())
print(data_queue.qsize())


# LifoQueue 구현
data_queue_lifo = queue.LifoQueue()
data_queue_lifo.put(10)
data_queue_lifo.put(20)
data_queue_lifo.put(30)
data_queue_lifo.put(40)

print(data_queue_lifo.qsize())
print(data_queue_lifo.get())   # 가장 나중 데이터인 40이 출력되는것을 확인

# PriorityQueue 데이터를 넣는 시간에 따른것이 아닌 우선순위에 따라 pop 되는 순서가 다르다.
data_queue_priority = queue.PriorityQueue()
data_queue_priority.put((10, "korea")) # 튜플형식으로 들어가며 "우선순위, 데이터" 이렇게 들어간다.
data_queue_priority.put((12, 1))
data_queue_priority.put((8, 402))
data_queue_priority.put((1, "china"))

print(data_queue_priority.get())  # 우선순위가 1인 china 가 출력되는 것을 확인할 수 있다. 따라서 숫자가 작을수록 우선순위가 크다
print(data_queue_priority.get())  # 그 다음 우선순위인 8에 대한 402가 출력된다.

# 연습 리스트로 큐의 기능 구현하기
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data
