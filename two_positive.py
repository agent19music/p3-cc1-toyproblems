#!/usr/bin/env python3

def two_positive(a, b, c):
    count = 0 # Initialize counter
    if a > 0: # Check if a is positive
        count += 1 # Increment counter
    if b > 0: # Check if b is positive
        count += 1 # Increment counter
    if c > 0: # Check if c is positive
        count += 1 # Increment counter
    print(count == 2) # Check if exactly 2 variables are positive

two_positive(9,7,0)