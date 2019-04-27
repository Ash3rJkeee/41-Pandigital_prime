import datetime
import PanDigitGener

# todo 0) написать генератор панцифровых чисел              ГОТОВО
# todo 1) написать функцию проверки числа на панцифровое ГОТОВО
# todo 2) написать проверку числа на простоту               ГОТОВО
# todo 3) написать поиск в диапазоне до 9876543210          ГОТОВО


def is_simple(x):
    """проверка на простоту по признакам делимости и по истинному определению"""

    """проверка по призканам делимости"""
    """по четности"""
    string = str(x)
    if int(string[-1]) % 2 == 0:
        return False

    """Делимость на 3"""
    sum_digits = 0
    for i in range(0, len(string)):
        sum_digits = sum_digits + int(string[i])
    if sum_digits % 3 == 0:
        return False

    """Делимость на 5"""
    if string[-1] == "0" or string[-1] == "5":
        return False

    """истинная проверка на простое число"""
    a = round(x**0.5)
    for i in range(2, a + 1):
        if x % i == 0:
            return False

    return True


def broot(n):
    global answer

    if n > 0:
        print("Начинаю поиск "+str(n)+"-значных.")
        myIter = PanDigitGener.pandigital_generator(n)

        try:
            while True:
                k = int(next(myIter))
                print('\r', end='')
                print(k, end='')
                if (is_simple(k)) and (k > answer):
                    answer = k
        except StopIteration:
            if answer != 0:
                return
            print('\n'+str(n)+"-значные варианты закончились")
            broot(n-1)
    else:
        return


answer = 0

print("Программа производит поиск максимального панцифрогоцо простого числа")

start = datetime.datetime.now()

broot(9)


stop = datetime.datetime.now()
estimate_time = stop - start

print("\nВычисления закончены и заняли:", estimate_time.seconds, "секунд.")
print("Ответ =", answer)




