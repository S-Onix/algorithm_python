# 최단 경로 알고르짐
# 최단 경로 문제 : 두 노드를 잇는 가장 짧은 경로를 찾는 문제
# 가중치 그래프에서 간선의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적

# 최단 경로 문제 종류
# 1. 단일 출발 및 단일 도착 최단 경로 문제
#   - 그래프 내의 특정 노드 u 에서 출발, 또다른 특정 노드 v에 도착하는 최단 경로를 찾는 문제
# 2. 단일 출발 최단 경로 문제
#   - 그래프 내의 특정 노드 u 와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제
# 3. 전체 쌍 최단경로 : 그래프 내의 모든 노드 쌍에 대한 최단 경로를 찾는 문제


# 다익스트라 알고리즘 : 2번에 해당하는 알고리즘이며, 하나의 정점에서 다른 모든 정점 간의 각각 가장 짧은 거리를 구하는 문제
# 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
# 다익스트라 알고리즘은 너비우선탐색과 유사하다

# heapq 라이브러리를 이용하여 우선순위 큐 사용하기
# min_heap  방식으로 구성된다 >> 우선순위가 최소인 것이 가장 첫번째로 올라온다.

import heapq

queue = []

heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
heapq.heappush(queue, [4, 'F'])
heapq.heappush(queue, [8, 'G'])

print(queue)

for index in range(len(queue)) :
    print(heapq.heappop(queue))
    # pop이 될때마다 최소 값으로 꺼내진다
    
# 그래프 표현
mygraph = {
    'A' : {'B' : 8, 'C' : 1, 'D' : 2},
    'B' : {},
    'C' : {'B' : 5, 'D' : 2},
    'D' : {'E' : 3, 'F' : 5},
    'E' : {'F' : 1},
    'F' : {'A' : 5}
}

def dijkstra(graph, start) :
    # 거리 저장 배열에 inf로 초기 세팅
    distances = {node: float('inf') for node in graph}

    print(distances)
    distances[start] = 0
    print(distances)

    queue = []
    heapq.heappush(queue, [distances[start], start])

dijkstra(mygraph, 'A')