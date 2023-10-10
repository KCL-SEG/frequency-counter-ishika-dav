"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

"""
def frequencies(items):
    frequencies = {}
    for item in items:  # Loop through all items directly
        frequency = 0  # Initialize the frequency of the current item
        for j in items:  # Check for duplicates of the current item
            if item == j:
                frequency += 1  # If there is a duplicate, increment frequency
        frequencies[item] = frequency  # Add item and its frequency to the dictionary
    return frequencies
"""

def frequencies(items):
    frequencies = {}
    for item in items:
        # convert item to its string representation to handle both strings + numbers
        str_item = str(item)
        if str_item in frequencies:
            frequencies[str_item] += 1
        else:
            frequencies[str_item] = 1
    return frequencies

frequency = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
print(frequency)

