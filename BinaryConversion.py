#!/usr/bin/env python3
"""
Date   : 2024-08-05
Purpose: Convert decimal integer to binary integer
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Decimal integer to binary integer Converter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('decimal',
                        metavar='decimal',
                        type=int,
                        help='A decimal integer')

    return parser.parse_args()

def main():
    """Calculator for decimal-to-binary Conversion"""

    args = get_args()
    dec = args.decimal

    def max_exponent(num):
        """Finds the largest power of 2 in the input integer and returns the exponent"""
        # Does NOT return the actual power. Just the corresponding exponent n in 2**n
        
        n=0
        while 2**n <= num:
            n += 1
        return n-1
    
    def digit(n):
        """Generates a binary digit from an exponent."""
        # This is quite a cheat method! It wouldn't be possible with other bases
        # because there can be multiple of the same digit. In binary this doesn't happen.

        x = 10**n
        return x
    
    num = dec           # Starting decimal integer
    total = 0           # Starting binary integer

    while max_exponent(num) > 0:                # Alternative: while num > 1:
        total += digit(max_exponent(num))           # Adds the largest binary digit
        num -= 2**max_exponent(num)                 # Removes the corresponding value from the decimal integer
    if num == 1:                                # Account for a remaining decimal integer of 1, terminate and print
        total += digit(max_exponent(num))
        print(str(total))  
    else:                                       # Terminate and print if remiaing decimal integer is 0
        print(str(total))

# --------------------------------------------------
if __name__ == '__main__':
    main()