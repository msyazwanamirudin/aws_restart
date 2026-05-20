def getDoubleAlphabet(alphabet):
    return alphabet + alphabet


# print(getDoubleAlphabet("a"))

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return int(shiftAmount)

def encryptMessage(message, key, alphabet):
    encryptedMessage = ""

    for currChar in message.upper():
        # print(currChar)
        position = alphabet.find(currChar)
        newPos = position + key
        # print(f"{currChar} actual position: {position}, new position {newPos}")
        encryptedMessage += alphabet[newPos]    

    return encryptedMessage

def decryptMessage(encryptedMsg, key, alphabet):
    msg = ""
    for currChar in encryptedMsg:
        position = alphabet.find(currChar)
        actualPos = position - key 
        msg = msg + alphabet[actualPos]
    
    return msg

msg = getMessage()
key = getCipherKey()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encryptedMsg = encryptMessage(msg, key, alphabet)
print(f"Encrypted message: {encryptedMsg}")
decryptedMsg = decryptMessage(encryptedMsg, key, alphabet)
print(f"Decrypte message: {decryptedMsg}")