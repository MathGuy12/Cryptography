def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterFrequencies = [0.0834, 0.0154, 0.0273, 0.0414, 0.126, 0.0203, 0.0192, 0.0611, 0.0671, 0.0023, 0.0087, 0.0424, 0.0253, 0.068, 0.077, 0.0166, 0.0009, 0.0568, 0.0611, 0.0937, 0.0285, 0.0106, 0.0234, 0.002, 0.0204, 0.0006]
    fout = open("data.txt", "w")
    n = int(input("Enter Max Keyword Lenght: "))
    message = textInput("Enter encrypted message:\n").upper()

    for i in message:
        if i not in alpha:
            message = message.replace(i,"")

    fout.write("Length\tAverage IOC\t\tIOC List\n")
    avgList = []

    for i in range(2, n + 1):
        chunks = ['' for x in range(i)]
        IOCs = ""
        c = 0
        
        for j in message:
            chunks[c] += j
            c = (c + 1) % i

        total = 0
        for j in chunks:
            x = frequencies(alpha, j)
            total += x
            IOCs += str(round(x,6)).ljust(8,'0') + "  "

        avg = round(total/i,6)
        avgList.append(avg)
        fout.write(str(i) + "\t\t" + str(avg).ljust(8,'0') + "\t\t" + IOCs + "\n")

    sortedAvgs = avgList.copy()
    sortedAvgs.sort(reverse=True)
    if sortedAvgs[0] > .04:
        maxIOC = avgList.index(sortedAvgs[0]) + 2
    else:
        maxIOC = "Likely Length Not Found"
    fout.write("\nLikely Keyword Length: " + str(maxIOC) + "\n")

    c = 0
    chunks = ['' for x in range(maxIOC)]
    for i in message:
        chunks[c] += i
        c = (c + 1) % maxIOC
    shifts = []        
    for i in chunks:
        shifts.append(likelyShift(i, alpha, letterFrequencies))
    fout.write("\nDecrypted and Encrypted Chunks:\n\n")
    decryptedChunks = []
    keyword = ""
    for i in range(maxIOC):
        decryptedChunks.append(performShift(chunks[i], shifts[i]))
        fout.write(decryptedChunks[i] + "\n")
        fout.write(chunks[i] + "\n\n")
        keyword += alpha[-1 * shifts[i]]
    fout.write("Likely Keyword: " + keyword + "\n")
    trueText = ""
    chunkInd = 0
    letterInd = 0
    while True:
        trueText += decryptedChunks[chunkInd][letterInd]
        if len(trueText.replace(" ", "").replace("\n","")) % 5 == 0:
            trueText += " "
        if len(trueText.replace(" ", "").replace("\n","")) % 50 == 0:
            trueText += "\n"
        chunkInd += 1
        if chunkInd == maxIOC:
            chunkInd = 0
            letterInd += 1
        if letterInd == len(decryptedChunks[chunkInd]):
            break
    fout.write("\nDecrypted and Reordered Text:\n\n" + trueText + "\n")

def frequencies(alpha, message):
    fTotal = 0
    for i in alpha:
        fTotal += message.count(i) * (message.count(i) - 1)
    return fTotal/(len(message) * (len(message) - 1))


def textInput(message):
    finalMessage = ""
    line = input(message)
    while line != "#":
        finalMessage += line
        line = input()
    return finalMessage


def likelyShift(message, alpha, letterFrequencies):
    sums = []
    for i in range(26):
        text = performShift(message, i)
        total = 0
        for j in range(26):
            total += letterFrequencies[j]*text.count(alpha[j])
        sums.append(total)
    sortedSums = sums.copy()
    sortedSums.sort(reverse=True)
    return sums.index(sortedSums[0])


def performShift(message, distance):
    if distance in [0,26]:
        return message
    shiftedText = ""
    for i in message:
        val = ord(i) + distance
        if val > ord('Z'):
            val += ord('A') - ord('Z') - 1
        shiftedText += chr(val)
    return shiftedText


if __name__ == "__main__":
    main()

"""
IZPHY XLZZP SCULA TLNQV FEDEP QYOEB SMMOA AVTSZ VQATL LTZSZ
AKXHO OIZPS MBLLV PZCNE EDBTQ DLMFZ ZFTVZ LHLVP MBUMA VMMXG
FHFEP QFFVX OQTUR SRGDP IFMBU EIGMR AFVOE CBTQF VYOCM FTSCH
ROOAP GVGTS QYRCI MHQZA YHYXG LZPQB FYEOM ZFCKB LWBTQ UIHUY
LRDCD PHPVO QVVPA DBMWS ELOSM PDCMX OFBFT SDTNL VPTSG EANMP
MJKAE PIEFC WMHPO MDRVG OQMPQ BTAEC CNUAJ TNOIR XODBN RAIAF
UPHTK TFIIG EOMHQ FPPAJ BAWSV ITSMI MMFYT SMFDS VHFWQ RQ
#
"""