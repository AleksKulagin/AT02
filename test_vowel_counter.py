import pytest
from vowel_counter import count_vowels

def test_all_vowels():
    # Строка, содержащая только гласные
    assert count_vowels("aeiou") == 5
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10
     

def test_no_vowels():
    # Строка, не содержащая гласных
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("БВГДЖЗКЛМНПРСТФХЦЧШЩ") == 0


def test_mixed_string():
    # Строка, содержащая смешанные символы (включая строчные и прописные гласные)
    assert count_vowels("Hello World!") == 3
    assert count_vowels("Привет, как дела?") == 5
    assert count_vowels("123!@#") == 0
    assert count_vowels("Python is Amazing!") == 5


if __name__ == '__main__':
    pytest.main()