def solution(arr1, arr2):
    answer = []
    o = []
    for (a, b) in zip(arr1, arr2):
        for (c, d) in zip(a, b):
            o.append(c + d)
        answer.append(o)
        o = []
    return answer
