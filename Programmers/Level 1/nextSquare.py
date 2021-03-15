import math

def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return pow(int(math.sqrt(n+1))+1,2)
    else:
        return -1
