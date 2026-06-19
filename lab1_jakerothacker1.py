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