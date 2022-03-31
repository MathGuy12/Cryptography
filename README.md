# Cryptography
A set of files used to encode and decode different ciphers
The PASC.py file is used for decoding polyalphabetic subsitution ciphers. The message input is terminated by a line with a single #. Uses index of coincidence calculations to determine key length and then letter frequencies on ceaser shifts to find most likely key word and correctly decoded message.

encryptDecrypt.py is a basic ceaser cipher function that will both encoded and decode messages.

encryptDecryptAdvanced.py is the the normal ceaser cipher encoder/decoder but extends beyond only lowercase letters to ASCII values 1 to 127. 

encryptDecryptExtra.py is similar to the normal ceaser cipher encoder/decoder, but the usuable charactes are the normal keyboard characters and the key shift is not constant. In other words, after the encoding of each character, the key will change based on another value given by the user.

keywordCipher.py is used for encoding and decoding keyword ciphers. The message input is terminated by a line with a single #. The file is also able to run frequency data on encrypted message, calculating freuqences for letters, bigrams, and trigrams. 
