# Password Protector - startkode
import hashlib


def hash_password(password):
    
    encoded_password = hashlib.sha256(password.encode())
    hashed_password = encoded_password.hexdigest()
    return hashed_password

password = input("Skriv inn et passord: ")


hashed_password = hash_password(password)


print("Originalt passord:", password)
print("Hashet passord:", hashed_password)