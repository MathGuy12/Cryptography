toContinue= "y"
while toContinue == "y":
    EcDc = str(input("Do you want to encrypt or decrpypt? "))
    if EcDc == "encrypt":
        plainText = input("Enter a lowercase message with no spaces: ")
        distance = int(input("Enter the distance value: "))
        code = ""
        for ch in plainText:
            ordValue = ord(ch)
            cipherValue = ordValue + distance
            if cipherValue > ord('z'):
                cipherValue = ord('a') + ordValue - ord('z') + distance - 1
            code += chr(cipherValue)
        print(code)
    elif EcDc == "decrypt":
        code = input("Enter the coded text: ")
        distance = int(input("Enter the distance value: "))
        plainText = ''
        for ch in code:
            ordValue= ord(ch)
            cipherValue = ordValue - distance
            if cipherValue < ord('a'):
                cipherValue = ord('z') + ordValue - ord('a') - distance + 1
            plainText += chr(cipherValue)
        print(plainText)
    else:
        print("\nINVALID ANSWER\n")
        print("Answer must be either 'encrypt' or 'decrypt'")
    toContinue= str(input("Do you wish to encrypt/decrypt again? 'y' or 'n' "))
