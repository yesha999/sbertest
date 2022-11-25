def yield_parts(num: int, last_num: int):
    if not num:
        yield ()

    for i in range(min(num, last_num), 0, -1):  # Цикл (1)
        for parts in yield_parts(num - i, i):  # Цикл (2), получает все возможные варианты разложения числа (кортежи),
            # включая те, которые не дают в сумме нужное число, но они не попадают в итоговый список генератора,
            # потому что последним падает необходимый кортеж
            yield (i,) + parts  # В итоговый список генератора попадает только последнее значение цикла (1)


def parts_count(num: int):
    if not (0 < num < 100):
        return 'Задайте число от 1 до 99'
    parts_list = list(yield_parts(num, num))
    return len(parts_list)


if __name__ == '__main__':
    print(parts_count(3))
