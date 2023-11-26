#!/usr/bin/env python3
def max_consonant(word):
    # Define the values of the letters
    values = {chr(i+97): i+1 for i in range(26)}
    
    # Initialize the maximum value and the current sum
    max_value, current_sum = 0, 0
    
    # Iterate over the characters in the string
    for char in word:
        # If the character is a consonant, add its value to the current sum
        if char not in 'aeiou':
            current_sum += values[char]
            # If the current sum is greater than the maximum value, update the maximum value
            if current_sum > max_value:
                max_value = current_sum
        # If the character is a vowel, reset the current sum
        else:
            current_sum = 0
            
    print(max_value)


