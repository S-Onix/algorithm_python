# 정렬 15분정도 풀이시간
# 나이, 이름, 가입 순서
# 나이를 Key값으로 주고 내부 value를 다시 diction으로 나눈다
# 구조 {22 : {idx : 1, name : xxx}, ....}
# 내부 diction들을 다 정렬한다 (기준 idx)
# 외부 diction들을 다 정렬한다 (기준 나이)
# 순서대로 전부 출력

def solve(num) :
    dict_set = list()
    for idx in range(0, num) :
        age, name = input().split(' ')
        dict_set.append({'age': int(age), 'idx' : idx, 'name' : name})
    
    inner_sorted = sorted(dict_set, key=lambda member: (member['age'], member['idx']))
    for d in inner_sorted :
        print(d['age'], d['name'])
    



solve(int(input()))