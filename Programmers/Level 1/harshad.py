def solution(x):
    answer = True
    div = 0
    li = list(str(x))
    for i in range(0,len(li)):
        div += int(li[i])
    if x % div ==0:
        answer = True
    else:
        answer = False
    return answer
