""" UPC-A validator

    Jake Rothacker

    This program validates a 12-digit UPC-A code by checking
    the last digit against the expected check digit from the first 11.

    Date:6/19/2026
    
"""


def find_UPC(upc11):
    """Finds the 12th digit of a UPC-A given the first 11 digits.



    Args:
        upc11 (str): The first 11 digits of the UPC-A code.
    """
    total = 0
    for i in range(11):
        if i % 2 == 0:
            total += int(upc11[i]) * 3
        else:
            total += int(upc11[i])
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)


status = True
while status ==True:


    upc = input("Please enter your 12-digit UPC: ")

    if upc == "quit":
        status = False
        continue
    elif len(upc) != 12 or not upc.isdigit():
        print("Invalid UPC. UPC entered was not a 12-digit number. Type 'quit' to exit.")
        continue

    upc11 = upc[:-1]
    upc12 = upc[-1]

    expected_upc12 = find_UPC(upc11)

    print("Expected UPC 12:", expected_upc12)
    print("Actual UPC 12:", upc12)
    if expected_upc12 == upc12:
        print("UPC is valid.")
    else:
        print("UPC is invalid.")