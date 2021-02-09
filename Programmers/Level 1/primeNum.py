def solution(n):
    answer = [True]*(n+1)
    count = 0
    root = int (n ** 0.5)
    for i in range(2, root+1):
        if answer[i]== True:
            for j in range(i+i,n+1,i):
                answer[j]=False
    for i in range(2,n+1):
        if answer[i]==True:
            count += 1
    return count
    
  
