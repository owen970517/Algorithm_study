def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n* factorial_recursive(n-1)

print('반복 : ' , factorial(5))
print('재귀 : ' , factorial_recursive(5))