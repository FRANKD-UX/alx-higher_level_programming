#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Attempt division
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            # Handle case where one of the elements is not an integer or float
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except IndexError:
            # Handle case where the list is too short
            print("out of range")
            result = 0
        finally:
            # Append the result (either successful division or 0)
            new_list.append(result)
    return new_list
