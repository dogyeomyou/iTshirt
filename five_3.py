# -*- coding: utf-8 -*-
# five_3.py
# 반복적으로 구현한 n! 함수
def factorial_itereative(n):
    result = 1 
    #n
    for i in range(1, n+1):
        result *= i
    return result

#재귀적그올 구현한 n! 함수 
def factorial_recursive(n):
    if n <= 1: #n이 1이하인 경우 1을 반환
        return 1
    #n! = n * (n-1)!를 그대로 코드로 작성한다.
    return n * factorial_recursive(n-1)
    result = 1
    
print("반복적으로 구현:", factorial_itereative(100))    
print("재귀적으로 구현:", factorial_recursive(100))

# -*- coding: utf-8 -*-
# five_5.py
# 반복적으로 구현한 n! 함수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
print(gcd(192,162))    