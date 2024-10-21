import os
from cryptography.fernet import Fernet

arquivos = []

# Carrega a chave secreta do arquivo
with open('chave.key', 'rb') as chave_file:
    secretkey = chave_file.read()

# Coleta todos os arquivos no diretório atual, exceto os especificados
for file in os.listdir():
    if file in {'MalwerKey.py', 'chave.key', 'DescriptArq.py'}:
        continue
    if os.path.isfile(file):
        arquivos.append(file)

# Descriptografa cada arquivo coletado
for file in arquivos:
    try:
        with open(file, 'rb') as arquivo:
            conteudo = arquivo.read()
        conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)
        with open(file, 'wb') as arquivo:
            arquivo.write(conteudo_decrypted)
        print(f"Arquivo {file} descriptografado com sucesso.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo {file}: {e}")
