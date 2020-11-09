import queue
# queue 라이브러리가 존재하며
# 1. Queue() : 가장 일반적인 큐 자료 구조
# 2. LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조)
# 3. PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

# 일반적인 큐 구현
data_queue = queue.Queue()
data_queue.put(10)
data_queue.put('Test')
print(data_queue.qsize())

print(data_queue.get())
print(data_queue.qsize())