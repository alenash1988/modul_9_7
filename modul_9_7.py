def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('Простое' if isprime(res) else 'Составное')
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c



result = sum_three(2, 3, 6)
print(result)
