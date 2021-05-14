import math


# A fibonacci series is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding
# numbers. The simplest is the series 1, 1, 2, 3, 5, 8

# Returns the fibonacci series
def gen_fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n-1):
        print(a, end=", ")
        c = a + b
        a = b
        b = c
    print(a)


# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square.

# A utility function that returns true if x is perfect square

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x


# Returns true if n is a Fibonacci Number, else false

def check_fibonacci(inputs_list):
    for n in inputs_list:
        if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
            print(f"{n} is a Fibonacci Element")
        else:
            print(f"{n} is NOT a Fibonacci Element")


def control():
    inputs = []
    print("Enter the number of elements you wanna check: ")
    n = int(input())
    print(f"Enter {n} elements : ")
    for i in range(n):
        k = int(input())
        inputs.append(k)
    check_fibonacci(inputs)


def main():
    print(" ============================ WELCOME TO THE FIBONACCI DOMAIN ============================ ")
    print("HOW CAN WE HELP YOU ?")
    print("Press 1 to generate a series of fibonacci elements ")
    print("Press 2 to check if a number is a fibonacci element ")
    choice = int(input())
    if choice == 1:
        print("Enter the range of your series ")
        n = int(input())
        gen_fibonacci(n)
    else :
        control()


if __name__ == '__main__':
    main()
