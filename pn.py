def is_prime(x):
    k = 0
    for i in range(2, 6):
        if (i**x - i) % x == 0:
            k = k + 1
        else:
            return False
    return True


if __name__ == "__main__":
    a = int(input("Введите проверяемое число: "))

    print(is_prime(a))
