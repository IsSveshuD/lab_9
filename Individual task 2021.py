#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {"a", "b", "g", "k", "m", "p"}
    B = {"b", "e", "f", "l", "r"}
    C = {"k", "l", "w", "x"}
    D = {"e", "j", "o", "p", "q", "u", "v"}

    x = (A.difference(B)).intersection(C.union(D))
    print(f"x = {x}")

    An = u.difference(A)
    Bn = u.difference(B)

    y = (An.intersection(Bn)).difference(C.union(D))
    print(f"y = {y}")
