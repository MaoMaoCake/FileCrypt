from Crypto.Cipher import AES

class Encryptor:
    def __init__(self,key=None):
        if key:
            try:
                # try to open the key file
                with open(key,'rb') as f:
                    self.key = f.read()
            except FileNotFoundError as e:
                # if keyfile does not exist  make a key file
                self.make_key()
                with open(key,'rb') as f:
                    self.key = f.read()
                print(e)

            self.cipher = AES.new(self.key,AES.MODE_EAX)
            self.nonce = self.cipher.nonce
        else:
            print("key empty")

    def encrypt(self,data=None):
        if data:
            data = data.encode()
            ciphertext, tag = self.cipher.encrypt_and_digest(data)
            return ciphertext,tag

    def decrypt(self,data=None,tag=None):
        if data :
            cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce)
            plaintext = cipher.decrypt(data)
            return plaintext

    def make_key(self):
        import os
        with open("key.bin",'wb') as f:
            f.write(os.urandom(32))