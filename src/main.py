


def fibonacci_recursive(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
      return 1
    else:
      return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

def fibonacci_loop(n):
    n1, n2 = 0, 1
    count = 2

    if n <= 0:
        return -1
    elif n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

    return nth

