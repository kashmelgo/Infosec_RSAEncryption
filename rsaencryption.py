#Kashmel Galil Go       BSCS

def rsaEncryptionAndDecryption(p,q,string):
    n = p * q
    z = (p-1) * (q-1)
    
    #e, less than n, which has no common factor (other than 1) with z
    for e in range(1,n):
        #finding GCD
        if( z % e != 0):
            break
            
    

    #Find number d, such that ed-1 is exactly divisible z
    for d in range(1,1000):
        if(d != z and (e*d-1) != z):
            if((e*d-1) % z == 0):
                break
    print(n)
    print(z)
    print(e)
    print(d)

    #public key (n, e)
    #private key (n, d)


    #encryption (m^e mod n) M IS ORIGINAL TEXT
    encryptedString = ''

    for i in range(len(string)):
        s = ord(string[i].upper())
        encryptedChar = chr((s**e % n))
        encryptedString += encryptedChar

    print(encryptedString)


    #decryption (c^d mod n) C IS ENCRYPTED/CIPHER
    decryptedString = ''
    for i in range(len(encryptedString)):
        s = ord(encryptedString[i])
        decryptedChar = chr((s**d % n)) 
        decryptedString += decryptedChar

    print(decryptedString)

    #decryptedString == originalText
 

def getNumber():
    return input("Input prime number: ")

def getString():
    return input("Input string: ")

#input p and q here and the string
p = int(getNumber())
q = int(getNumber())
string = getString()

rsaEncryptionAndDecryption(p,q,string)
