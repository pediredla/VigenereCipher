#import detectEnglish, vigenereCipher, pyperclip
#import enchant
import time

def main():
    userInput = input("Enter the string (enclose with double quotes) you want to encrypt: ")
    keyInput = input("Enter the key (enclose with double quotes) you want to encrypt with: ")
    encrypt = encryptText(userInput,keyInput)
    print encrypt

    cipher = input("Enter the cipher text (enclose with double quotes): ")
    keyLength = input("Enter the key length: ")
    firstWordLength = input("Enter the first word length: ")
    iteratableHash = bruteForce(keyLength,cipher,firstWordLength)

    print iteratableHash
# function to encrypt given text using Vigenere cipher
def encryptText(text, key):
    res = ""
    text = text.upper()
    key = key.upper()
    y = 0
    for x in xrange(0,len(text)):
        c = str(text[x])
        if (c < 'A' or c > 'Z'):
            continue
# From algeberic description of Vigenere cipher, source: Wikipedia
        # res += (char)((c + key.charAt(j) - 2 * 'A') % 26 + 'A')
        #print chr((ord(c)+ord((key[y]))-2*ord('A'))%26 + ord('A'))
        res += chr(((ord(c) + ord(str(key[y])) - 2*ord('A'))%26) + ord('A'))
        y = (y+1) % len(key)
    return res

def decryptText(text, key):
    res = ""
    text = text.upper()
    y = 0
    for x in xrange(0,len(text)):
        c = str(text[x])
        if(c < 'A' or c > 'Z'):
            continue
# From algeberic description of Vigenere cipher, source: Wikipedias
            #res += (char)((c - key.charAt(j) + 26) % 26 + 'A')
        res +=chr(((ord(c)-ord(str(key[y])) + 26)) % 26 + ord('A'))
        y = (y+1) % len(key)

    return res

def keyGen(keylength):
	#generate key with given length
	alphabet = []
	for x in xrange(65,91):
		alphabet.append(chr(x))
	if keylength == 0: return []

	key = [[a] for a in alphabet[:]]
	if keylength == 1: return key

	key = [[x,y] for x in alphabet for y in alphabet]
	if keylength == 2: return key

	for l in range(2, keylength):
		key = [[x]+y for x in alphabet for y in key]

	return key

def bruteForce(keylength,cipher,firstWordLength):
    #read from the dictionary
    words = set()
    with open('dict.txt') as f:
        for line in f:
            words.add(line.strip())
    #use bruteforce attack with the keys generated, use hashmap to store
    #dictionary = enchant.Dict("en_US")
    hashmap = {}
    for key in keyGen(keylength):
        attempt = decryptText(cipher,''.join(key))
        if attempt[:firstWordLength] in words:
            hashmap = {''.join(key):attempt}

    return hashmap

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
