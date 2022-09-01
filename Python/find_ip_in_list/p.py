# t : 텍스트
# p : 패턴
# N : 텍스트의 길이
# M : 패턴의 길이

def BruteForce(t, p):
    N = len(t); M = len(p)
    i = 0 # 텍스트 인덱스
    j = 0 # 패턴 인덱스
    while i < N and j < M:
    	if t[i] != p[i]: # 다르면
            i = i - j # i를 시작 위치로 되돌린다.
            j = -1 # j를 -1로 설정
        i += 1
        j += 1
    if j == M : # 패턴을 찾음
        return i - M # 패턴이 시작하는 위치를 반환
    else : return -1