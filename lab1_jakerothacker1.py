status = True
while status ==True:


    upc = input("Please enter your 12-digit UPC: ")

    if upc == "quit":
        status = False
        continue
    elif len(upc) != 12 or not upc.isdigit():
        print("Invalid UPC. UPC entered was not a 12-digit number. Type 'quit' to exit.")
        continue


