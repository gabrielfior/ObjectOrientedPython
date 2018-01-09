"""
Helper static functions for other classes
"""

def get_valid_input_string(input_string, valid_options):
    """
    Validates input of the user, so that it enters one of the required answers, or is prompted again.
    :param input_string:
    :param valid_options:
    :return:
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response