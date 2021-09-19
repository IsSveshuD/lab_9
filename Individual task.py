#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {"a", "e", "f", "i"}
    B = {"a", "b", "k", "n"}
    C = {"e", "f", "n", "o", "w", "x"}
    D = {"a", "d", "e", "o", "p", "t", "u"}

    x = (A.union(B)).intersection(D)
    print(f"x = {x}")

    An = u.difference(A)
    Bn = u.difference(B)

    y = (An.intersection(Bn)).difference(C.union(D))
    print(f"y = {y}")
