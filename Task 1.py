#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s = input("Введите строку:")
    count = 0
    vowels = {'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
    for letter in s:
        if letter in vowels:
            count += 1
    print("Количество гласных равно:")
    print(count)
