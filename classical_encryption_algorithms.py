
import string


alphabet = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

def brutForceAttack(outputStr, maxLength, plainText):
    if(len(outputStr) == maxLength):
        return
    for char in plainText:
        temp = outputStr + char
        print(temp)
        brutForceAttack(temp, maxLength, plainText)


brutForceAttack('', 3, 'abc')






#####................Encryption and Decryption of Caesar-Cipher with equation................#####
def EncryptCaesarCipher(plainText, key):
    cipherText = ''
    for plainTextLetter in plainText:
        asci = ord(plainTextLetter) # convert to unicode code e.g: a = 97
        cipherText += chr(asci+key) # convert unicode code to character e.g: 100 = c
    return cipherText

def DecryptCaesarCipher(cipherText, key):
    plainText = ''
    for cipherTextLetter in cipherText:
        asci = ord(cipherTextLetter)
        plainText += chr(asci-key)
    return plainText

cipherText = EncryptCaesarCipher('this is plainText with some symbols @#$% ^_^ &**(*(' , 15)
print('Caesar-Cipher with equation..')
print( 'cypherText is: ', cipherText)
plainText = DecryptCaesarCipher(cipherText , 15)
print( 'plainText is: ', plainText)
print('\n')


#####................Encryption and Decryption of Caesar-Cipher with shifting................#####
def encryptionCaesarCipherShifting(plainText):
    encryptionText = ''
    for plainTextLetter in plainText:
        asci = ord(plainTextLetter)
        encryptionText += chr(asci + 3)
    return encryptionText

def decryptionCaesarCipherShifting(cypherText):
    plainText = ''
    for cypherTextLetter in cypherText:
        asci = ord(cypherTextLetter)
        plainText +=  chr( asci - 3 )
    return plainText

cypherText = encryptionCaesarCipherShifting('this is plainText with some symbols @#$% ^_^ &**(*(')
plainText = decryptionCaesarCipherShifting(cypherText)
print('CaesarCipher with shifting..')
print("cypherText is ", cypherText)
print("plainText is ",  plainText)
print('\n')




#####................Encryption and Decryption of vigenere................#####

# use keywordStr function to generate the repetition of a key 
# plaintext:  It will encrypt with vigenere algorithm 
# key:        CIPHER                                   => 5
# repetition: CIPHERCIPHERCIPHERCIPHERCIPHERCIPHERCIP  => 39
def vigenereKeywordStr(plainText, keyword):
    keywordStr = ''
    for i in range( int(len(plainText)/len(keyword))+1 ):
        keywordStr += keyword
        if len(keywordStr) > len(plainText):
            keywordStr = keywordStr[: len(plainText) - len(keywordStr) ]
    return keywordStr
    
def vigenereEncryption(plainText, keyword):
    keyStr = vigenereKeywordStr(plainText, keyword)
    cipherText = ''
    for i in range(len(plainText)):
        newIndex = alphabet.find(plainText[i]) + alphabet.find(keyStr[i])
        cipherText += alphabet[newIndex % len(alphabet)]
    return cipherText

def vigenereDecryption(cipherText, keyword):
    keyStr = vigenereKeywordStr(str(cipherText), keyword)
    plainText = ''
    for i in range(len(cipherText)):
        newIndex = alphabet.find(cipherText[i]) - alphabet.find(keyStr[i])
        plainText += alphabet[newIndex % len(alphabet)]
    return plainText

cipherText = vigenereEncryption('It will encrypt with vigenere algorithm', 'CIPHER') # (space) isn't in alphabet array so, it will encrypt to the latest alphabet (Z)
print('Vigenere Cipher...')
print('cipherText is ', cipherText)
plainText = vigenereDecryption(cipherText, 'CIPHER')
print('plainText is ', plainText)
print('\n')



#####................Encryption and Decryption of affineCipher................#####
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modInverse(a):
    m = 26
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def affineCipherEncryption(plainText, k1, k2):
    cipherText = ''
    for plainTextLetter in plainText:
        newIndex = (k1*alphabet.find(plainTextLetter) + k2) % len(alphabet)
        cipherText += alphabet[newIndex]
    return cipherText
def affineCipherDecryption(cypherText, k1, k2):
    plainText = ''
    for cypherTextLetter in cypherText:
        newIndex = (modInverse(k1)) * (alphabet.find(cypherTextLetter) - k2) % len(alphabet)
        plainText += alphabet[newIndex]
    return plainText
print('Affine Cipher....')
cipherText = affineCipherEncryption('This is plainText', 7, 10) # (space) isn't in alphabet array so, it will encrypt to the latest alphabet (Z)
print('cipherText is ', cipherText)
plainText = affineCipherDecryption(cipherText, 7, 10)
print('plainText is ', plainText)
print('\n')





#####................Encryption and Decryption of Transposition Cipher................#####
def transpositionEncryption(plainText, depth):
    cypherText = ''
    lines = [''] * depth
    for lineIndex in range(len(lines)):
        i = lineIndex
        for _ in plainText: # use underscore because i don't need to use this variable
            newValue = lines[lineIndex] + plainText[i]
            lines[lineIndex] = newValue
            if(i<len(plainText)-depth):
                i += depth
            else: break
    # print(lines)
    for cypherTextLines in lines:
        cypherText += cypherTextLines
    return cypherText
def transpositionDecryption(cypherText, depth):
    plainText = ''
    lines = []
    # split cipherText to rows
    start = 0
    for _ in range(depth): # use underscore because i don't need to use this variable
        end = start + int(len(cypherText)/depth) +1
        lines.append( cypherText[ start: end ] )
        if start < len(cypherText):
            start = end
    # print(lines)
    for lettersIndex in range( len(lines[0]) ):
        for linesIndex in range(depth):
            if len(lines[linesIndex]) > lettersIndex:
                plainText += lines[linesIndex][lettersIndex]
            else: break
    return plainText

print('Transposition Cipher...')
transpositionEncryption1 = transpositionEncryption( 'hello this is plainText', 4)
print('CypherText is =>',transpositionEncryption1)
transpositionDecryption1 = transpositionDecryption(transpositionEncryption1, 4)
print('PlainText is =>',transpositionDecryption1)

