
def solution(s):
    if(len(s) > 8 or len(s) < 1):
        return False
    else:
        return s.isdigit() and len(s) in (4,6)
