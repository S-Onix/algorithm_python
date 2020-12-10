# 깊이 우선 탐색 DFS(Depth First Search) : 정점의 자식들을 먼저 탐색하는 방식
#   - 방문 큐(visited)와 데이터를 쌓아줄 스택(need_visit)을 이용함

graph2 = dict()
graph2['A'] = ['B', 'C']
graph2['B'] = ['A', 'D']
graph2['C'] = ['A', 'G', 'H', 'I']
graph2['D'] = ['B', 'E', 'F']
graph2['E'] = ['D']
graph2['F'] = ['D']
graph2['G'] = ['C']
graph2['H'] = ['C']
graph2['I'] = ['C', 'J']
graph2['J'] = ['I']

def dfs(graph, start_node) :
    visited,need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit :
        node = need_visit.pop()
        if node not in visited :
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

print(dfs(graph2, 'A'))