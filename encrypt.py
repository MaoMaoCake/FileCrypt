from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self,key=None):
        if key:
            try:
                # try to open the key file
                with open(key,'rb') as f:
                    self.key = f.read()
            except FileNotFoundError as e:
                # if keyfile does not exist  make a key file
                self.make_key(key)
                with open(key,'rb') as f:
                    self.key = f.read()
                print(e)
                print("Created Key File")

            self.cipher = Fernet(self.key)
        else:
            print("key empty")

    def encrypt(self,data=None):
        if data:
            data = data.encode()
            ciphertext = self.cipher.encrypt(data)
            return ciphertext

    def decrypt(self,data=None,tag=None):
        if data :
            plaintext = self.cipher.decrypt(data)
            return plaintext

    def make_key(self,name):
        with open(name,'wb') as f:
            f.write(Fernet.generate_key())