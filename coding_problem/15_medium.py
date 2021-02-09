# Z / 재귀함수 / 40분

# 방문 순서 찾기 (2^(n-1) * 2^(n-1))의 크기


# 좌표 >> 0,0 > 2,2 까지
# 0   1 4   5
# 2   3 6   7
# 8   9 12 13
# 10 11 14 15

# 확장되는 구조
# x,y 좌표를 다 가지고 있어야함
# 이동하는 방식에 대한 로직이 있어야함

# 최종적으로 방문 순서 -1 (1부터 시작하기 위해서)

def next_visit(n, x, y) :
    global visit_cnt
    # 탈출 조건(r,c 와 x, y의 값이 일치할 경우)
    if n == 2:
        if x == r and y == c :
            print(visit_cnt)
            return
        visit_cnt += 1
        if x == r and y+1 == c :
            print(visit_cnt)
            return
        visit_cnt += 1
        if x+1 == r and y == c :
            print(visit_cnt)
            return
        visit_cnt += 1
        if x+1 == r and y+1 == c :
            print(visit_cnt)
            return
        visit_cnt += 1
        return
    
    # x,y 위 위치가 4*4 의 맵에서 (0,0) / (2,0) / (0,2) / (4,4) 의 경우에 대한 재귀함수 호출
    next_visit(n/2, x, y)
    next_visit(n/2, x + n/2, y)
    next_visit(n/2, x, y + n/2)
    next_visit(n/2, x + n/2, y + n/2)
        


N, r, c = map(int, input().split(' '))
visit_cnt = 0
next_visit(N, 0, 0)