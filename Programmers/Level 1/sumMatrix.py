def solution(arr1, arr2):
    # t = []
    # answer = []
    # for i,j in zip(arr1,arr2):
    #     for x,y in zip(i,j):
    #         t.append(x+y)
    #     answer.append(t)
    #     t=[]
    # return answer
    return [[x+y for x,y in zip(i,j) ] for i,j in zip(arr1,arr2)]
