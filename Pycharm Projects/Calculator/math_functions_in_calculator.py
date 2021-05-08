import math


def addition(x, y):
    sum_of_variables = x + y
    return sum_of_variables


def subtraction(x, y):
    diff_of_variables = x - y
    return diff_of_variables


def multiplication(x, y):
    prod_of_variables = x * y
    return prod_of_variables


def division(x, y):
    div = x / y
    return div


def modulo_division(x, y):
    div = x % y
    return div


def power_of_num(x, y):
    return math.pow(x, y)


def square_root_of_num(x):
    return math.sqrt(x)


def gcd(x, y):
    return math.gcd(x, y)


# ========================================== Trigonometric Functions ===================================================
def sine(k):
    return math.sin(math.radians(k))


def cosine(k):
    return math.cos(math.radians(k))


def tangent(k):
    return math.tan(math.radians(k))


a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd Number"))
add = addition(a, b)
print(add)

print(math.trunc(2.99))
print(math.ceil(-2.99))
print(math.floor(-2.99))


