#!/usr/bin/python3


def text_indentation(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty result string
    result = ""

    # Iterate through each character in the text
    for char in text:
        result += char  # Add the current character to the result
        # Check if the current character is one of the specified characters
        if char in '.?:':
            result += "\n\n"  # Add two new lines after the character

    # Split the result by lines and print each line
    # without leading or trailing spaces
    for line in result.splitlines():
        print(line.strip())

# Example usage


text_indentation
("Hello world. How are you? I hope you're doing well: let's meet soon.")
