def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if n //i == i:
                answer += i
            else:
                answer += n//i + i

    return answer
