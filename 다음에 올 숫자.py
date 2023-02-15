# 다음에 올 숫자 


# 문제 설명

# 등차수열 혹은 등비수열 common이 매개변수로 주어질때 ,마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요


# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 4]는 공차가 1인 등차수열이므로 다음에 올 수는 5이다.
# 입출력 예 #2

# [2, 4, 8]은 공비가 2인 등비수열이므로 다음에 올 수는 16이다




def solution(common):
    answer = 0
    a, b ,c = common[:3]
    #common이 등차수열일 때
    if b - a == c - b:
        answer = common[-1] +(b - a)
    #common이 등비수열일 때
    elif b // a == c // b:
        answer = common[-1] * (b // a)
    return answer