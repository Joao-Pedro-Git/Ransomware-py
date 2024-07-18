from importlib.resources import contents
import os 
from cryptography.fernet import Fernet


arquivos = []

key = Fernet.generate_key()


with open('chave.key' , 'rb') as key:
    secretkey = key.read()


for file in os.listdir():
    if file == 'MalwerKey.py' or file == 'chave.key' or file == 'DescriptArq.py':
        continue
    if os.path.isfile(file):
        arquivos.append(file)


for file in arquivos:
    with open(file, 'rb') as arquivo:
        conteudo = arquivo.read()
    conteudo_dencrypted = Fernet(secretkey).decrypt(conteudo)
    with open(file, 'wb') as arquivo:
        arquivo.write(conteudo_dencrypted)
