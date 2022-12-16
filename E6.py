import argparse
from Crypto.Hash import SHA256, MD5

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en MD5')

parser.add_argument("username",help="el nombre del fichero a encriptar y comparar con entrada2", type=str)

parser.add_argument("password",help="el nombre del fichero a encriptar y comparar con entrada2", type=str)

args = parser.parse_args()

hashedPassword = SHA256.new(bytes(args.password,'utf-8'))

line = args.username +":"+ hashedPassword.hexdigest()+"\n"



with open("shadow","r") as f:
    
    strings = f.read().split("\n")

    for i in strings:
        if(i.__contains__(args.username)):
            print("El usuario ya existe")
            exit()
            

with open("shadow","a") as f:
    f.write(line)
    

