def solution(num):
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        cnt += 1
        if num == 1:
            break
    return cnt if cnt < 500 else -1
