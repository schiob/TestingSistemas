#!/bin/python3

import sys

def solve(grades):
    rounded = []
    for g in grades:
        if g < 38:
            rounded.append(g)
        else:
            if g % 5 > 2:
                rounded.append(5 * (g//5 +1))
            else:
                rounded.append(g)
    return rounded

if __name__ == '__main__':
    n = int(input().strip())
    grades = []
    grades_i = 0
    for grades_i in range(n):
       grades_t = int(input().strip())
       grades.append(grades_t)
    result = solve(grades)
    print ("\n".join(map(str, result)))
