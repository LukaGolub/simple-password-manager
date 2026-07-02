from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import hashlib
import sys

salt = b"simetriranjelab1"
key = PBKDF2("lab1mp", salt, dkLen=16)
i = "delete lab1mp"


def encrypt(password, adress):
    password = password.ljust(256, '\0').encode()
    cipher = AES.new(key, AES.MODE_EAX)
    cipher.update(adress.encode())
    ciphertext, tag = cipher.encrypt_and_digest(password)
    nonce = cipher.nonce
    return ciphertext, tag, nonce




print("Password manager initialized.")
f = open("lab1passwords.txt", "a")
while True:
    
    i = input("> ")
    if i == "exit":
        print("Exiting password manager...")
        sys.exit()

    try:
        command = i.split()[0]
        mp = i.split()[1]
        
    except IndexError:
        print("Master password incorrect or integrity check failed.")
        continue
    

    if mp != "lab1mp":
         print("Master password incorrect or integrity check failed.")
         continue
    if command == "put":
            adress = i.split()[2]
            pw, tag, nonce = encrypt(i.split()[3], adress)
            hash_adress = hashlib.sha256((adress + "tajna").encode()).hexdigest()
            pair = f"{hash_adress} {pw.hex()} {tag.hex()} {nonce.hex()}"

            
            try:
                with open("lab1passwords.txt", "r") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                lines = []

            found = False
            new_lines = []

            for line in lines:
                if line.startswith(hash_adress + " "):
                    new_lines.append(pair + "\n")
                    found = True
                else:
                    new_lines.append(line)

            if not found:
                new_lines.append(pair + "\n")

            
            with open("lab1passwords.txt", "w") as f:
                f.writelines(new_lines)

            print(f"Stored password for {adress}.")

    elif command == "get":
            adress = i.split()[2]
            hash_adress = hashlib.sha256((adress + "tajna").encode()).hexdigest()
            found = False
            for line in open("lab1passwords.txt"):
                if line.startswith(hash_adress):
                    ciphertext = bytes.fromhex(line.split()[1])
                    tag = bytes.fromhex(line.split()[2])
                    nonce = bytes.fromhex(line.split()[3])
                    try:
                            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
                            cipher.update(adress.encode())
                            pw = cipher.decrypt_and_verify(ciphertext, tag)
                            print(f'Password for {adress} is: {pw.decode().strip("\0")}')
                            found = True
                            break 
                    except (ValueError, KeyError):
                            found = False
                            continue
            if found == False:
                 print("Master password incorrect or integrity check failed.")
                 
                
                    


    elif command == "delete":
            print("Are you sure you want to delete your password database? This will delete all passwords [Y/N].")
            j = input()
            if j == "Y":
                print("Deleting all passwords from database.")
                with open("lab1passwords.txt", "r+") as f:
                    f.seek(0)
                    f.truncate()
                    
            elif j == "N":
                    print("Aborting password deletion.")
                    continue
            else:
                    print("Master password incorrect or integrity check failed.")
                    continue
            
    else:
         print("Master password incorrect or integrity check failed.")
         continue
         
   

    




