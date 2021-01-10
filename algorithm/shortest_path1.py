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
    print('step 1 ::: ')
    print(distances)            # {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf} 로 설정됨

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = 0
    # 모든 정점이 저장될 큐를 생성
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start], start])

    print('step 2 ::: ')
    print(queue)            # {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf} 로 설정됨
    
    i = 2

    while queue :
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_node = heapq.heappop(queue)
        i+=1
        print('step',i,' ::: ')
        print('heappop ::: ',current_distance, current_node)

        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_node] < current_distance :
            continue

        for adjacent, weight in graph[current_node].items() :
            #현재 해당되는 노드까지의 가중치 + 도착지에 대한 가중값을 더한 값
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent] :
                # 거리를 업데이트한다.
                distances[adjacent] = distance
                heapq.heappush(queue,[distance, adjacent])
                i+=1
                print('step',i,' ::: ')
                print('queue ::: ', queue)
                print('distances ::: ' , distances)

    # path = end
    # path_output = end + '->'
    # while distances[path][1] != start :
    #     path_output += distances[path][1] + '->'
    #     path = distances[path][1]
    # path_output += start
    # print(path_output)

    return distances


print(dijkstra(mygraph, 'C'))
