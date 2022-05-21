from cryptography.fernet import Fernet


class Encrypt:
    def __init__(self):
        self.key = self._get_key()
        self.cipher = self._get_cipher()

    def _get_key(self):
        key = Fernet.generate_key()
        return key
    def _get_cipher(self):
        cipher = Fernet(self.key)
        return cipher

    def encrypt(self,data=None):
        data = bytes(data,encoding='utf-8')
        result = self.cipher.encrypt(data)
        return result
    def decrypt(self,data):
        result = self.cipher.decrypt(data)
        return result

    def encrypt_file(self,filepath):
        with open(filepath,"rb") as file:
            file_data = file.read()
            result = self.cipher.encrypt(file_data)
        with open(filepath,"wb") as file:
            file.write(result)
    def decrypt_file(self,filepath):
        with open(filepath,"rb") as file:
            file_data = file.read()
            result = self.cipher.decrypt(file_data)
        with open(filepath,"wb") as file:
            file.write(result)


