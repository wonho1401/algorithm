def solution(n):
    answer = 0
    r = []
    while n >= 0:
        r.append(n%3)
        if n ==1 or n ==2:
            break
        n = n // 3
    for i in range(len(r)):
        answer += r[i]*3**(len(r)-i-1)
    return answer
