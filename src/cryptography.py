from cryptography.fernet import Fernet
import os
class Crypto:
    def __init__(self):
        self.key = None
        self.dest = os.path.join()
        
    def generateKey(self):
        self.key = Fernet.generate_key()
        with open("pass.key", "wb") as key_file:
            key_file.write(self.key)
            
            
            
    def callKey(self):
        return open("pass.key","rb").read()
    
    def encode(self, code):
        key = self.callKey()
        encoded = code.encode()
        a = Fernet(key)
        encrypted = a.encrypt(encoded)
        return encrypted
    
    def decrypt(self, code):
        key = self.callKey()
        b = Fernet(key)
        decoded = b.decrypt(code)
        return decoded