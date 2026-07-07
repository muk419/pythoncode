"""A small demo: Fibonacci sequence and prime check."""


def fibonacci(n):
    """Return the first n Fibonacci numbers."""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def is_prime(num):
    """Return True if num is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("First 10 Fibonacci numbers:")
    print(fibonacci(10))

    print("\nPrime numbers from 1 to 20:")
    print([n for n in range(1, 21) if is_prime(n)])
