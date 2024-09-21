def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through each element in the original list
    for element in my_list:
        # If the element matches the search value, append the replace value
        if element == search:
            new_list.append(replace)
        else:
            # Otherwise, append the original element
            new_list.append(element)

    return new_list


# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 2, 5]
    search = 2
    replace = 9

    print(search_replace(my_list, search, replace))
