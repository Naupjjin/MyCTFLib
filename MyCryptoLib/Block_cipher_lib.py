from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import string


class BLOCKcipher:

    def prepend_oracle(LENGTH: int,BLOCK: int, oracle):
        pass
    
    def padding_oracle():
        pass

    def bit_flipping():
        pass

class ECB:
    '''
    ciphertext = encrypt_ecb(plaintext, key)
    print(f"Encrypted: {ciphertext}")

    decrypted_plaintext = decrypt_ecb(ciphertext, key)
    print(f"Decrypted: {decrypted_plaintext}")
    '''
    @staticmethod
    def encrypt_ecb(plaintext, key):

        cipher = AES.new(key, AES.MODE_ECB)
        padded_plaintext = pad(plaintext.encode(), AES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        
        return ciphertext

    @staticmethod
    def decrypt_ecb(ciphertext, key):
    
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_padded_plaintext = cipher.decrypt(ciphertext)

        return decrypted_padded_plaintext

class CBC:
    '''
    ciphertext_cbc = CBC.encrypt_cbc(plaintext, key, iv)
    decrypted_cbc = CBC.decrypt_cbc(ciphertext_cbc, key)
    print(f"CBC Mode - Encrypted: {ciphertext_cbc}\nDecrypted: {decrypted_cbc}")
    '''
    @staticmethod
    def encrypt_cbc(plaintext: str, key: bytes, iv: bytes):
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = pad(plaintext.encode(), AES.block_size)

        ciphertext = cipher.encrypt(padded_plaintext)
        return iv + ciphertext  

    @staticmethod
    def decrypt_cbc(ciphertext: bytes, key: bytes):
        iv = ciphertext[:AES.block_size]  
        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted_padded_plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        plaintext = unpad(decrypted_padded_plaintext, AES.block_size)

        return plaintext.decode()
    

