def count_vowels(s):
    """
    Функция подсчёта количества гласных в строке.
    :param s: Исходная строка
    :return: Количество гласных букв
    """
    vowels = "aeiouаеёиоуыэюя"
    return sum(1 for char in s.lower() if char in vowels)