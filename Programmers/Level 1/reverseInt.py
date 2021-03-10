def solution(n):
    answer = 0
    arr = sorted(list(str(n)),reverse=True)
    answer = int("".join(arr))
    return answer
