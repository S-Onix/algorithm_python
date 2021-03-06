# 최소 신장 트리

# Spanning Tree, 또는 신장 트리 라고 불림
# 원래의 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프
# 신장 트리의 조건
#   본래의 그래프의 모든 노드를 포함해야 함
#   모든 노드가 서로 연결
#   트리의 속성을 만족시킴(사이클 존재 x)

# 최소 신장 트리
# MST (Minimum Spanning Tree)
# 신장 트리 중에서 간선의 가중치합이 가장 최소인 트리를 지칭함

# 최소 신장 트리를 찾을 수 있는 대표적인 두가지 알고리즘이 존재함 (가장 중요한 것은 사이클을 형성하지 않는 것)
# Kruskal's algorithm (크루스칼 알고리즘), Prim's algorithm(프림 알고리즘)

# 간선의 가중치를 오름차순으로 정렬한다.
# 가중치가 작은 간선부터 양 끝의 두 정점을 비교한다.
# 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.(사이클이 생기지 않도록 하는 것)

# Union Find 알고리즘
# Disjoint Set을 표현할 때 사용하는 알고리즘으로 트리 구조를 활요하는 알고리즘
# 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 사용
# Disjoint Set
#   서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
#   공통 원소가 없는 (서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함
#   Disjoint Set = 서로소 집합 자료구조

# 3가지 연산이 필요
# INIT : N개의 원소가 각각 개별 집합으로 이뤄지도록 초기화
# UNION : 두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 합침
# FIND : 여러 노드가 존재할 때, 두개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지
# 판별하기 위해, 각 그룹의 최상단 원소(즉, 루트 노드)를 확인
#   주의점 트리를 잘못 구성할 경우 linked_list 형식의 모든 원소를 찾아야 하는 가능성이 존재함
#   이름 해결하기위 union-by-rank, path compression 기법을 사용함
# union-by-rank : 각 트리에 대한 높이(rank)를 기억하고 두 트리의 높이가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임
# 높이가 h-1인 두 개의 트리를 합칠때에는 한 쪽 트리의 높이를 1 증가시키고, 다른 쪽의 트리를 해당 트리에 붙여준다


graph = {
    'vetices' : ['A','B','C', 'D', 'E', 'F', 'G'], # 노드
    # 노드간의 가중치 (무방향이므로 모두 적어줘야한다.)
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (9, 'B', 'D'),
        (8, 'B', 'C'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]    # 간선
}

#Union By Rank 기법을 사용하기 위한 자료구조를 설정한다.
# 각각 노드의 부모노드를 저장함
parent = dict()
# 각각 노드의 랭크를 저장하기 위함
rank = dict()

def make_set2(node) :
    parent[node] = node
    rank[node] = 0

def find2(node) :
    if parent[node] != node :
        parent[node] = find2(parent[node])
    return parent[node]

def union2(node_v, node_u) :
    # 두 노드의 root노드를 찾아온다 (합쳐주기 위해서)
    root1 = find2(node_v)
    root2 = find2(node_u)

    if rank[root1] > rank[root2] :
        parent[root2] = root1
    else :
        parent[root1] = root2
        if rank[root1] == rank[root2] :
            rank[root2] += 1



def kru2(graph) :
    mst = list()
    # 1. 초기화
    # Union-Find 를 하기 위해서 각 부분집합을 만들어야한다.
    for node in graph['vetices'] :
        make_set2(node)
    
    # 2. 간선 weight 기반 sorting
    #가중치를 정렬해준다.
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결(사이클 없는 것에 대해서)
    # 가중치가 낮은 것부터 꺼냄
    for edge in edges :
        #양끝 노드를 찾아옴
        weight, node_v, node_u = edge
        #사이클 여부를 검사하기 위해서 :: 루트가 동일하다면 이어주면 안되고 스킵되어야한다.
        if find2(node_v) != find2(node_u) :
            union(node_v, node_u)
            mst.append(edge)

    return mst

def make_set(node) :
    parent[node] = node
    rank[node] = 0

def find(node) :
    # path compression
    if parent[node] != node :
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u) :
    # 두 노드의 root 노드를 찾아온다.
    root1 = find(node_v)
    root2 = find(node_u)

    # UNION by rank 기법 사용
    if rank[root1] > rank[root2] :
        parent[root2] = root1
    else :
        parent[root1] = root2

        if rank[root1] == rank[root2] :
            rank[root2] += 1

def kruskal(graph) :
    mst = list()

    # 노드를 전체 순회하며 초기화해야함
    for node in graph['vetices'] :
        make_set(node)

    # 간선의 가중치에 대해서 크기가 작은 순으로 정렬해준다
    edges = graph['edges']
    edges.sort()

    # 가중치가 낮은 간선부터 비교함
    for edge in edges :
        #  edge의 구성은 (가중치, 노드1, 노드2) 로 구성되어 있으므로 아래와 같이 표현 가능함
        weight, node_v, node_u = edge
        # node_v의 root노드와 node_u의 root 노드가 다를 경우 두 개의 트리를 합쳐준다.
        if find(node_v) != find(node_u) :
            union(node_v, node_u)
            mst.append(edge)

    return mst

print(kru2(graph))


parent2 = dict()
rank2 = dict()


def find3(node) :
    if parent2[node] != node :
        parent2[node] = find3(parent2[node]) 
    return parent2[node]

def union3(node_v, node_u) :
    # 두 노드의 루트를 찾고
    root1 = find3(node_v)
    root2 = find3(node_u)

    if rank2[root1] > rank2[root2] :
        # 랭크가 작은 루트 노드의 부모는 랭크가 큰 노드로 변경된다
        parent2[root2] = root1
    else :
        parent2[root1] = root2
        if rank2[root1] == rank2[root2] :
            rank2[root2] += 1
 
def kruskal2(graph) :
    mst = list()

    # 초기화를 해야함 > 원소를 분리하여 parent와 rank를 지정해야함
    for node in graph['vetices'] :
        parent2[node] = node
        rank2[node] = 0

    # 초기화 이후 가중치에 대한 sorting이 필요함
    edges = graph['edges']
    edges.sort()

    # 정렬된 가중치순서로 노드를 이어주기 시작한다
    for edge in edges :
        weight, node_v, node_u = edge

        # 루트의 일치여부 검사 (일치하면 사이클 / 일치하지 않으면 연결해줘야함)
        if find3(node_v) != find3(node_u) :
            # 루트를 찾아 연결해줘야한다. (union by rank 기법사용하기)
            union3(node_v, node_u)
            mst.append(edge)

    return mst


print(kruskal2(graph))

    