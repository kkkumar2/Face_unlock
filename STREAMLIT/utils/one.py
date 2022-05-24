# from cryptography.fernet import Fernet
# import pandas as pd
# import os
# import pickle
# from dotenv import load_dotenv
# from dotenv import load_dotenv
# import os

# # key = Fernet.generate_key()

# # key = key.decode()
# # print(key)
# # os.environ['CIPHER_KEY'] = key

# # c_key = os.environ.get('CIPHER_KEY')
# # c_key = bytes(c_key,'utf-8')
# # cipher = Fernet(c_key)

# # data = cipher.encrypt(b"Jesus")

# # data2 = cipher.decrypt(data)

# # print(data)
# # print("data2 is",data2)

# # load_dotenv()
# # c_key = os.getenv('SECRET_KEY')
# # print("c_key is",c_key)
# # c_key = bytes(c_key,'utf-8')
# # cipher = Fernet(c_key)
# # data = cipher.encrypt(b"Jesus")
# # data2 = cipher.decrypt(data)

# # print(data2)

from cryptography.fernet import Fernet
import pandas as pd
import os
import pickle
from dotenv import load_dotenv
from encrypt import Encrypt

# class Encrypt:
#     def __init__(self):
#         load_dotenv()
#         self.secrets_path = os.path.join('DATA','Metadata','secrets.pkl')
#         self.file_cipher = os.getenv('SECRET_KEY')

#     def get_key(self):
#         key = Fernet.generate_key()
#         return key
#     def get_cipher(self,key):
#         cipher = Fernet(key)
#         return cipher

# obj1 = Encrypt()
# # key = obj1.get_key().decode()
# # print(key)

# load_dotenv()
# file_cipher = bytes(os.getenv('SECRET_KEY'),'utf-8')
# file_cipher = obj1.get_cipher(file_cipher)
# print(file_cipher)
# userdata = file_cipher.encrypt(b"jesus")
# print(userdata)
# data = file_cipher
# with open("useless.pkl", 'wb') as file:
#     pickle.dump(data, file)
# df = pd.read_pickle("useless.pkl")
# ciph = df
# print(ciph)
# print(df.decrypt(userdata))
unique_id = 1
data1 = pd.read_pickle("usedata.pkl")
data1 = data1['data']
obj1 = Encrypt()
out = obj1.decrypt_data(unique_id,data1)
print(out)

print(out.decode())