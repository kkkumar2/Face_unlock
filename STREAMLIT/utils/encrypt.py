from cryptography.fernet import Fernet
import pandas as pd
import os
import pickle
from dotenv import load_dotenv

class Encrypt:
    def __init__(self):
        self.key = self._get_key()
        self.cipher = self._get_cipher()
        self.secrets_path = os.path.join('DATA','Metadata','secrets.pkl')
        self.secret_key = os.path.join('DATA','Metadata','secret_key.pkl')
        self.file_cipher = None

    def _get_key(self):
        key = Fernet.generate_key()
        return key
    def _get_cipher(self):
        cipher = Fernet(self.key)
        return cipher

    def update_key_cipher(self,unique_id,type=None): ## This is for existing users who have already generated a key

        df = pd.read_pickle(self.secrets_path)
        if unique_id in df.keys():
            self.cipher = df[unique_id]
            self.key = ""
        elif type != None:
            return False
        else:
            df[unique_id] = self.cipher
            with open(self.secrets_path, 'wb') as f:
                pickle.dump(df, f)
            self.encrypt_file(self.secrets_path)

    def encrypt(self,unique_id=None,userdata=None):
        if self.file_cipher == None:
            self.secret_key_gen()
        if not os.path.exists(self.secrets_path):
            data = {unique_id: self.cipher}
            with open(self.secrets_path, 'wb') as f:
                pickle.dump(data, f)
            self.encrypt_file(self.secrets_path)
        self.decrypt_file(self.secrets_path)

        result = []
        self.update_key_cipher(unique_id)
        if type(userdata) == "list":
            for ele in userdata:
                ele = bytes(ele,encoding='utf-8')
                result.append(self.cipher.encrypt(ele))
            return result,self.cipher
        else:
            result = self.cipher.encrypt(data)
            return result

    def decrypt(self,unique_id,data):
        self.decrypt_file(self.secrets_path)
        result = []
        status = self.update_key_cipher(unique_id,"while_decrpt")
        if type(data) == "list":
            for ele in data:
                result.append(self.cipher.decrypt(ele))
            return result,self.cipher
        else:
            result = self.cipher.decrypt(data)
            return result

    def encrypt_file(self,filepath):
        with open(filepath,"rb") as file:
            file_data = file.read()
            result = self.file_cipher.encrypt(file_data)
        with open(filepath,"wb") as file:
            file.write(result)

    def decrypt_file(self,filepath):
        with open(filepath,"rb") as file:
            file_data = file.read()
            result = self.file_cipher.decrypt(file_data)
        with open(filepath,"wb") as file:
            file.write(result)


    def secret_key_gen(self):
        if not os.path.exists(self.secret_key):
            data = {"key": self.cipher}
            with open(self.secret_key, 'wb') as file:
                pickle.dump(data, file)
            self.key = self._get_key()
            self.cipher = self._get_cipher()
        
        file_data = pd.read_pickle(self.secret_key)
        self.file_cipher = file_data["key"]