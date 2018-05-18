from cryptography.fernet import Fernet

def getMessage():
    plaintextMessage = raw_input("What is the message you would like to encrypt?")
    return plaintextMessage

def generateKey():
    key = Fernet.generate_key()
    #print "Your symetric key is "+ key + " guard it with your life!"
    return key


generateKey()

cipherSuite = Fernet(generateKey())
cipherText=cipherSuite.encrypt(getMessage())



def decrypt():
    decryptedText = cipherSuite.decrypt(cipherText)
    return decryptedText

print "this is your encrypted version of the message " + cipherText
print "this is the message back in plaintext" + decrypt()