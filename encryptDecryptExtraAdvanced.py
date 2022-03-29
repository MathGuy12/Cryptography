
def main():

    #allows while loop to begin
    toContinue = "y"

    #loops only while toContinue is equal to 'y'
    while toContinue == "y":

        #asks user if they want to encode or decode
        EcDc = input("Do you want to encrypt or decrpypt? ")

        #block for encoding
        if EcDc == "encrypt":

            #user inputs and begining string for coded message
            plainText = input("Enter a message: ")
            key = int(input("Enter the key value: "))
            change = int(input("Enter the key change value: "))
            code = ""

            #for loop cycling through the input message
            for ch in plainText:

                #ensures key is small enough to keep characters in the typable range
                if key > 94:
                    key %= 94
                    
                #converts the characters to numbers and adds the key value
                ordValue = ord(ch)
                cipherValue = ordValue + key

                #ensures cipherValue is in the range of typable characters
                if cipherValue > ord('~'):
                    
                    cipherValue = ord(" ") + (key - ord('~') + ordValue - 1)

                #Converts the cypherValue to a character and adds to string
                code += chr(cipherValue)

                #Changes key for extra security
                key += change
                key **= change
                
            print(code)

        #block for decoding
        elif EcDc == "decrypt":

            #user inputs and begining string for decoded message
            code = input("Enter the encoded text: ")
            key = int(input("Enter the key value: "))
            change = int(input("Enter the key change value: "))
            plainText = ''

            #loops through encoded message
            for ch in code:

                #ensures key is small enough to keep characters in the typable range
                if key > 94:
                    key %= 94

                #converts the characters to numbers and subtracts the key value
                ordValue= ord(ch)
                cipherValue = ordValue - key

                #ensures cipherValue is in the range of typable characters
                if cipherValue < ord(" "):
                    
                    cipherValue = ord('~') - (key + ord(" ") - ordValue-1)

                #Converts the cypherValue to a character and adds to string    
                plainText += chr(cipherValue)

                #Changes key for extra security
                key += change
                key **= change
                
            print(plainText)

        #block if incorrect input    
        else:
            
            print("\nINVALID ANSWER\n")
            print("Answer must be either 'encrypt' or 'decrypt'")

        #asks user if they wish to continue    
        toContinue= input("\nDo you wish to encrypt/decrypt again? 'y' or 'n' ")
        print()

#runs main function when run from this file
if __name__ == '__main__':
    main()
