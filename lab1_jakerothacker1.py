""" UPC-A validator

    Jake Rothacker

    This program validates a 12-digit UPC-A code by checking
    the last digit against the expected check digit from the first 11.

    Date:6/19/2026
    
"""

def find_UPC(upc11):
    """Finds the 12th digit of a UPC-A given the first 11 digits.



    Args:
        upc11 (str): The first 11 digits of the UPC-A code. MUST BE AN 11-DIGIT STRING.

    Returns:
        str: The expected 12th digit of the UPC-A code.
    """
    total = 0
    for i in range(11):
        if i % 2 == 0:
            total += int(upc11[i]) * 3
        else:
            total += int(upc11[i])
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)

def validate_input(input):
    """checks if the input is 12-digits

    Args:
        input (str): Any string

    Returns:
        bool: True if the input is a 12-digit number, False otherwise.
    """
    if len(input) != 12 or not input.isdigit():
        return False
    return True

def print_results(expected, actual):
    """Prints the expected and actual UPC 12 digits.

    Args:
        expected (str): The expected 12th digit.
        actual (str): The actual 12th digit.
    """
    print("Expected UPC 12:", expected)
    print("Actual UPC 12:", actual)
    if expected == actual:
        print("UPC is valid.")
    else:
        print("UPC is invalid.")

def upc_check(upc):
    """Takes input and checks if it is a valid UPC-A

    Args:
        12_digit_upc (str): Any string works, but it should be a 12-digit number.

    Returns:
        bool: True if the input is a valid UPC-A, False otherwise.
    """
    if not validate_input(upc):
        print("Invalid UPC. UPC entered was not a 12-digit number. Type 'quit' to exit.")
        return False

    upc11 = upc[:-1]
    upc12 = upc[-1]

    expected_upc12 = find_UPC(upc11)
    print_results(expected_upc12, upc12)
    if expected_upc12 == upc12:
        return True
    else:
        return False

status = True
while status ==True:

    upc = input("Please enter your 12-digit UPC: ")

    if upc == "quit":
        status = False
        continue
    upc_check(upc)
        