#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    st1 = input('Введите первую строку:')
    st2 = input('Введите вторую строку:')
    it = set(st1) & set(st2)
    print(', '.join(it))
