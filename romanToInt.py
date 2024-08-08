#!/usr/bin/env python3
"""
Date   : 2024-08-05
Purpose: Numeral to Integer Converter
"""
        # This calculator works correctly for valid Roman Numerals
        # but will successfully attempt to convert invalid Roman Numerals too, e.g., XIIII or XIIV
        # In particular, it works if _any_ numeral value is less than its successor,
        # but should only work if it is a unit down e.g. IV and IX allowed but IL and VX not allowed

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Numeral to Integer Converter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numeral',
                        metavar='numeral',
                        help='A Roman Numeral')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Calculator for Numeral-to-Integer Conversion"""

    args = get_args()
    numeral = args.numeral

    def convSingle(l):
        if l == 'I':
            return 1
        elif l == 'V':
            return 5
        elif l == 'X':
            return 10
        elif l == 'L':
            return 50
        elif l == 'C':
            return 100
        elif l == 'D':
            return 500
        elif l == 'M':
            return 1000

    ans = 0
    for i, s in enumerate(numeral):                 # Alternative: for i in range(len(numeral))
        if i < len(numeral)-1:
            if convSingle(s) >= convSingle(numeral[i+1]):
                ans += convSingle(s)
            elif convSingle(s) < convSingle(numeral[i+1]):
                ans -= convSingle(s)
        else:
            ans += convSingle(s)
    print(ans)

# --------------------------------------------------
if __name__ == '__main__':
    main()