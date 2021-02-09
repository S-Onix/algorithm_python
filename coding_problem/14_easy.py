# 피보나치 수
# 15분
# 재귀함수

def fibo(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else :
        return fibo(n-2) + fibo(n-1)

def fibo2(n) :
    cache = [0 for x in range(n+1)]

    cache[0] = 0
    cache[1] = 1

    for idx in range(2, n+1) :
        print(idx)
        cache[idx] = cache[idx-2] + cache[idx-1]

    print(cache)
    return cache[-1]

print(fibo2(int(input())))