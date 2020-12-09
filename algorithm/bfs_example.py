# 너비 우선 탐색 BFS(Breadth First Search) : 같은 레벨의 노드들을 먼저 탐색하는 방식
#   - 방문 큐와 데이터를 쌓아줄 큐 두개를 이용함
# 깊이 우선 탐색 DFS(Depth First Search) : 정점의 자식들을 먼저 탐색하는 방식


def bfs(graph, start_node) :
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit :
        node = need_visit.pop(0)
        if node not in visited :
            need_visit.extend(graph[node])
            
    return visited

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

visited = bfs(graph, 'A')
print(visited)