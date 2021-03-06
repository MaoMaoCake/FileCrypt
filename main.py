from encrypt import Encryptor



e = Encryptor(key = "key.bin")

text = input("Text to encrypt:")

with open("file.encrypt","wb") as f:
    text_and_tag = e.encrypt(text)
    f.write(text_and_tag[0])

with open("file.encrypt","rb") as f:
    x = f.read()
    print(e.decrypt(x).decode())