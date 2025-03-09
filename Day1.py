# Factorial of a Number
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5)) 
# 120


# Fibonacci Sequence
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Palindrome Check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("Madam"))  # True
