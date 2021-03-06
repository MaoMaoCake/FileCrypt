from encrypt import Encryptor

class MainApp:
    def __init__(self,key_file):
        self.e = Encryptor(key=key_file)

    def encrypt_file(self,text,file_name="file.encrypt"):
        with open(file_name, "wb") as f:
            text_and_tag = self.e.encrypt(text)
            f.write(text_and_tag)

    def decrypt_file(self,file_name):
        with open(file_name, "rb") as f:
            x = f.read()
            print(self.e.decrypt(x).decode())

    def encrypt_directory(self):
        pass

    def decrypt_directory(self):
        pass

key_file = input("Key file location:")

text = input("Text to encrypt:")
file_name = "hi.encrypted"

m = MainApp(key_file=key_file)
m.encrypt_file(text=text,file_name=file_name)
m.decrypt_file(file_name=file_name)