import re


def finder():
    with open('task1-en.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    words_before_dot = re.findall(r'\b(?!\d+\b)\w+(?=\.)', text)
    fractions = re.findall(r'\b\d+\.\d+\b', text)

    return words_before_dot, fractions


words, fractions = finder()
print("Слова перед точкой:", words)
print("Дробные числа:", fractions)
