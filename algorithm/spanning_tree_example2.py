# 프림 알고리즘
# 크루스칼과 비교 
# 크루스칼 : 간선을 추출하여 가중치를 정렬하여 가장 낮은 가중치를 가진 노드들을 연결함(사이클을 형성되지 않게)
# 프림 : 기준 노드와 연결된 노드들 중 가장 가중치가 낮은 노드와 연결하여 트리를 만들어간다.(사이클 형성되지 않게)
# 둘다 탐욕 알고리즘을 기초로 하고 있다.(당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)

# 순서
# 1. 임의의 정점을 선택, '연결된 노드 집합'에 삽입
# 2. 선택된 정점에 연결된 간선들을 간선 리스트에 삽입
# 3. 간선 리스트에서 최소 가중치를 가지는 간선부터 추출해서,
#     - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면, 스킵함(사이클 방지)
#     - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않다면, 해당 간선을 선택하고, 해당 간선 정보를 '최소 신장 트리'에 삽입 
# 4. 추출한 간선은 간선 리스트에서 제거
# 5. 간선 리스트에 더 이상의 간선이 없을 때까지 3~4번을 반복

# heapq.heappush
# heapq.heappop
import heapq

queue = []
# 가중치, 노드로 구성된 리스트 구성
graph_data = [[2,'A'],[5,'B'],[3,'C']]

# 리스트를 통으로 넣어주면서 최소 heap 구조로 만들어줌
heapq.heapify(graph_data)

for index in range(len(queue)) :
    print(heapq.heappop(queue))

print(queue)

# collections 라이브러리의 defaultdict 함수 활용하기
# defaultdict 함수를 사용하여, key에 대한 value 지정 없이 빈 리스트로 초기화가 가능하다

from collections import defaultdict

list_dict = defaultdict(list)
print(list_dict['key'])



# 1. 모든 간선의 정보를 저장한다(adjacent edges)
# 2. 임의의 정점을 선택, '연결된 노드 집합(connected_nodes)'에 삽입
# 3. 선택된 정점에 연결된 간선들을 간선 리스트(candidate_edge_list)에 삽입
# 4. 간선 리스트에서 최소 가중치를 가지는 간선부터 추출(heapq.heappop)
#   - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면 스킵(cycle 방지)
#   - 해당 간선에 연결된 인접 정점이 '연뎔된 노드 집합'에 들어 있지 않으면, 해당 간산을 선택하고,
#     최소 신장 트리에 삽입    
# 5. 추출한 간선은 간선 리스트에서 제거 (heappop)
# 6. 간선 리스트에 더 이상 간선이 없을때 까지 4~5번을 반복한다.

# 간선은 중복해서 만들어줄 필요가 없다 (7,'A','B') (7,'B','A') >> 둘중 하나만 그리기
edges = [
    (7,'A','B'), (5,'A','D'),
    (8,'B','C'), (9,'B','D'), (7,'B','E'),
    (5,'C','E'),
    (7,'D','E'), (6,'D','F'),
    (8,'E','F'), (9,'E','G'),
    (11,'F','G')
]

from collections import defaultdict
import heapq

# 임의의 정점 start_node
def prim(start_node, edges) :
    # 최소신장트리 저장 리스트
    mst = list()
    
    # 모든 간선 정보를 저장하기 위한 로직
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges :
        adjacent_edges[n1].append(weight, n1, n2)
        adjacent_edges[n2].append(weight, n2, n1)

    # 최초 임의로 선택한 노드를 '연결된 노드 집합'에 추가
    connected_nodes = set(start_node)
    # start_node와 연결된 간선들을 간선 리스트에 저장
    candidate_edge_list = adjacent_edges[start_node]

    # 최소 힙 큐에 데이터를 일괄 저장한다
    heapq.heapify(candidate_edge_list)

    # 연결된 간선을 가진 리스트가 빌때까지 계속 반복한다.
    while candidate_edge_list :
        weight, n1, n2 = heapq.heappop(candidate_edge_list) # 가중치가 가장 작은 데이터가 추출
        # 검출되지 않는 노드일 경우 아래를 진행
        if n2 not in connected_nodes :
            # 연결 노드 리스트에 노드 추가
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2] :
                if edge[2] not in connected_nodes :
                    heapq.heappush(candidate_edge_list, edge)

    return mst
         