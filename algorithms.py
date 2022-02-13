# receive m y n and return m = q * n + r
def rest_theorem(m: int, n: int):
    """

    :type m: int
    :type n: int
    """
    q = m // n
    r = m % n
    return f'{m} = {q} * {n} + {r}'


# mcd
def mcd(a: int, b: int):
    """

    :type a: int
    :type b: int
    """

    if b == 0:
        return a
    return mcd(b, a % b)


def mcm_euclides(a: int, b: int):
    """

    :type a: int
    :type b: int
    """

    if a == 0 or b == 0:
        return 0

    return mcd(a, b) / a * b


# is prime
def is_prime(num: int):
    """

    :type num: int
    """
    if num <= 0:
        return False
    elif (num % 1) != 0:
        return False

    if num == 2 or num == 3:
        return True
    elif num % 2 == 0:
        return False

    square_root = int(num ** 0.5)

    for number in range(3, square_root + 1, 2):
        if num % number == 0:
            return False

    return True


# Finds prime factors of a number
def prime_factors(num: int):
    """

    :type num: int
    """
    arr = []

    while num != 1:
        for number in range(2, num+1):
            if num % number == 0:
                num //= number
                arr += number,
                break

    return arr


# find mcd of some numbers
def mcd_some(*a):

    commons_mcd = [prime_factors(number) for number in a]
    total_commons = {number for common in commons_mcd for number in common}

    # set accumulator
    final_mcd = 1

    for number in total_commons:
        is_number_in_all = [number in common for common in commons_mcd]
        if all(is_number_in_all):
            count_number = min([common.count(number) for common in commons_mcd])
            final_mcd *= number ** count_number

    return final_mcd


# find mcm of some numbers
def mcm_some(*a):

    commons_mcm = [prime_factors(number) for number in a]
    total_commons = {number for common in commons_mcm for number in common}

    # set accumulator
    final_mcm = 1

    for number in total_commons:
        count_number = max([common.count(number) for common in commons_mcm])
        final_mcm *= number ** count_number

    return final_mcm


# find relatives primes
def relative_primes(a: int, b: int):
    """

    :type a: int
    :type b: int
    :return: bool
    """
    commons = set(prime_factors(a)).intersection(set(prime_factors(b)))
    if commons:
        return False
    return True


print(relative_primes(4, 8))
