def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer +="*"
    answer= answer+phone_number[-4:]
    return answer
  
  // "*"* (len(phone_number)-4) 를 이용하면 for문 안써도 됐다..
