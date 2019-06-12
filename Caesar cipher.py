while True:
    choice = input("E or D (refer to ENCODE and DECODE)\n")
    if choice == "D":
        ciphertext = input("Please enter the \nciphertext: ")
        plaintext = ""
        ask = 0
        for i in ciphertext:
            ask = ord(i) - 3
            if ask < 65:
                ask = ask + 26
            if ask > 90 and ask < 97:
                ask = ask + 26
            plaintext += chr(ask)
        print("plaintext:  " + plaintext)

    if choice == "E":
        plaintext = input("Please enter the \nplaintext:  ")
        ciphertext = ""
        ask = 0
        for i in plaintext:
            ask = ord(i) + 3
            if ask > 90 and ask < 97:
                ask = ask - 26
            if ask > 122:
                ask = ask - 26
            ciphertext += chr(ask)
        print("ciphertext: " + ciphertext)