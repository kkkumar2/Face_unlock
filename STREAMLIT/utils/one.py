from cryptography.fernet import Fernet
import pandas as pd
import os
import pickle
from dotenv import load_dotenv


key = Fernet.generate_key()
cipher = Fernet(key)

os.environ['CIPHER_TRY'] = cipher

f = os.environ.get('CIPHER_TRY')

data = f.encrypt("Jesus")

f.decrypt("data")