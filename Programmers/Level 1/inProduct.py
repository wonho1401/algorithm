def solution(a, b):
    answer = 0
    for i in range(0,len(a)):
        answer += a[i]*b[i]
    return answer

  
  // zip함수 사용 -> 새로운 순서쌍 탄생
  // zip(a,b) => (a[0],b[0]), (a[1],b[1]) , ..
