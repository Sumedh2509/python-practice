import random 
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#Encrypting
def encrypt():

    plain_text = input("Please enter the message you want to encrypt:  ")
    encrypted_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        encrypted_text += key[index]

    print(f"plain text : {plain_text}\n",f"Encrypted text : {encrypted_text}")

#Decrypting

def decrypt():
    encrypted_text = input("Please enter the message you want to decrypt:  ")
    plain_text = ""

    for letter in encrypted_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted text: {encrypted_text}\n",f"Decrypted text: {plain_text}")

def main():
    is_running =  True
    while is_running:
        choice = input("Do you want encrypt or decrypte your message?(E/D):").upper()
        if choice == 'E':
            encrypt()
        else:
            decrypt()
        if input("Do you want to keep using?(Y/N): ").upper() != 'Y':
            is_running = False


if __name__ == '__main__':
    main()