def solution(numbers):
    answer = []
    s = 0
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if i == j:
                continue
            s = numbers[i]+numbers[j]
            if s not in answer:
                answer.append(s)
    return sorted(answer)
    
    
    // set를 활용해서 바로 중복 없애기
    // from itertools import combinations -> combinations(numbers,2)
