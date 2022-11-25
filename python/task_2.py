def is_prime(num: int) -> bool:
    """
    Проверяет простое ли число.
    """
    for i in range(2, num // 2 + 1):  # От двух до тех пор, пока число при делении может получить 2
        if (num % i == 0):  # Если поделилось, значит число непростое
            return False
    return True


def prime(num: int) -> bool:
    if num <= 1:  # Числа меньше единицы не могут быть простыми-близнецами
        return False
    if is_prime(num):
        upper_value = num + 2
        if is_prime(upper_value):
            return True
        lower_value = num - 2
        if is_prime(lower_value):
            return True
    return False


if __name__ == '__main__':
    list_of_prime_twins_numbers = []
    for i in range(50):
        if prime(i):
            list_of_prime_twins_numbers.append(i)
    print(list_of_prime_twins_numbers)
