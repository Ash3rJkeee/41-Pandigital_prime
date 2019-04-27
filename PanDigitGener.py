def pandigital_generator(n):
    """
    Генератор панцифровых значений
    :param n:
    :return:
    """
    array_0 = list(range(n, 0, -1))
    number = list(range(n, 0, -1))

    def string_number(in_number: list):
        """Компонует из листа итоговое значение числа"""
        string_number = ""
        for i in range(0, len(in_number)):
            string_number = string_number + str(in_number[i])
        return string_number

    for zero in array_0:
        number[0] = zero

        if len(number) > 1:
            array_1 = array_0[:]
            array_1.remove(zero)

            for first in array_1:
                number[1] = first

                if len(number) > 2:
                    array_2 = array_1[:]
                    array_2.remove(first)

                    for second in array_2:
                        number[2] = second

                        if len(number) > 3:
                            array_3 = array_2[:]
                            array_3.remove(second)

                            for third in array_3:
                                number[3] = third

                                if len(number) > 4:
                                    array_4 = array_3[:]
                                    array_4.remove(third)

                                    for four in array_4:
                                        number[4] = four

                                        if len(number) > 5:
                                            array_5 = array_4[:]
                                            array_5.remove(four)

                                            for fifth in array_5:
                                                number[5] = fifth

                                                if len(number) > 6:
                                                    array_6 = array_5[:]
                                                    array_6.remove(fifth)

                                                    for sixth in array_6:
                                                        number[6] = sixth

                                                        if len(number) > 7:
                                                            array_7 = array_6[:]
                                                            array_7.remove(sixth)

                                                            for seventh in array_7:
                                                                number[7] = seventh

                                                                if len(number) > 8:
                                                                    array_8 = array_7[:]
                                                                    array_8.remove(seventh)

                                                                    for eighth in array_8:
                                                                        number[8] = eighth

                                                                        if len(number) > 9:
                                                                            array_9 = array_8[:]
                                                                            array_9.remove(eighth)

                                                                            for ninth in array_9:
                                                                                number[9] = ninth

                                                                                yield string_number(number)
                                                                        else:
                                                                            yield string_number(number)
                                                                else:
                                                                    yield string_number(number)
                                                        else:
                                                            yield string_number(number)
                                                else:
                                                    yield string_number(number)
                                        else:
                                            yield string_number(number)
                                else:
                                    yield string_number(number)
                        else:
                            yield string_number(number)
                else:
                    yield string_number(number)
        else:
            yield string_number(number)
    return "Перебраны все варианты"


if __name__ == "__main__":
    myIter = pandigital_generator(10)

    while True:
        print(next(myIter))
        input()
