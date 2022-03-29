def main():
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    cont1 = 'y'
    while cont1 == 'y':
        cont2 = 'y'
        keyword = input("Enter keyword: ").upper().replace(" ", "")
        keyword = "".join(dict.fromkeys(keyword))
        shift = createCipher(keyword, alpha)
        while cont2 == 'y':
            action = input("Encrypt or Decrypt or Frequencies? (e/d/f): ").lower()[0]
            if action == 'e':
                encrypt(alpha, shift)
            elif action == 'd':
                decrypt(alpha, shift)
            elif action == 'f':
                frequencies(alpha)
            else:
                print("Invalid Response")
                continue
            cont2 = input("Do you wish to use this keyword again? (y/n) ").lower()[0]
        cont1 = input("Do you wish to create a new keyword? (y/n) ").lower()[0]

def createCipher(keyword, alpha):
    shift = []

    for i in keyword:
        if i in alpha:
            shift.append(i)

    for i in alpha:
        if i not in shift:
            shift.append(i)
    
    return shift

def encrypt(alpha, shift):
    message = textInput("Enter message: ").upper()
    cipherText = ""
    count = 0
    for i in message:
        if i not in alpha:
           continue
        else:
            cipherText += shift[alpha.index(i)]
            count += 1
        if count % 5 == 0:
            cipherText += " "
    
    print("Encoded message:", cipherText, sep="\n")

def decrypt(alpha, shift):
    message = textInput("Enter encoded message: ").upper()
    cipherText = ""
    count = 0
    for i in message:
        if i not in alpha:
           continue
        else:
            cipherText += alpha[shift.index(i)]
            count += 1
        if count % 5 == 0:
            cipherText += " "
    
    print("Encoded message:", cipherText, sep="\n")

def frequencies(alpha):
    fTotal = 0
    message = textInput("Enter message: ").upper().replace(" ", "")
    print("\nSINGLE LETTER FREQUENCIES")
    print("LETTER\tCOUNT\tFREQUENCY")
    for i in alpha:
        print(i, message.count(i), "%.02f" % (100 * message.count(i)/len(message)), sep= '\t')
        fTotal += message.count(i) * (message.count(i) - 1)
    
    print("\nIndex of Coincidence = %0.5f" % (1/(len(message) * (len(message) - 1)) * fTotal))
    

    
    bigrams = []
    print("\nBIGRAM FREQUENCIES")
    print("BIGRAM\tCOUNT\tFREQUENCY")
    for i in range(len(message) - 1):
        bigram = message[i] + message[i+1]
        if message.count(bigram) < 5 or bigram in bigrams:
            continue
        bigrams.append(bigram)
        print(bigram, message.count(bigram), "%.02f" % (100 * message.count(bigram)/(len(message) - 1)), sep= '\t')

    trigrams = []
    print("\nTRIGRAM FREQUENCIES")
    print("TRIGRAM\tCOUNT\tFREQUENCY")
    for i in range(len(message) - 2):
        trigram = message[i] + message[i+1] + message[i+2]
        if message.count(trigram) < 5 or trigram in trigrams:
            continue
        trigrams.append(trigram)
        print(trigram, message.count(trigram), "%.02f" % (100 * message.count(trigram)/(len(message) - 2)), sep= '\t')

def textInput(message):
    finalMessage = ""
    line = input(message)
    while line != "#":
        finalMessage += line
        line = input()
    return finalMessage

if __name__ == "__main__":
    main()