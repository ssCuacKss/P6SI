import argparse
from Crypto.Hash import SHA256, MD5
import random
import string

parser = argparse.ArgumentParser(description='introduce usuarios en el fichero shadow con contraseña encriptada')

parser.add_argument("username",help="nombre de usuario", type=str)

parser.add_argument("password",help="contraseña de usuario", type=str)

args = parser.parse_args()

salt = random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)

hashedPassword = SHA256.new(bytes(salt+args.password,'utf-8'))

line = args.username +":"+ hashedPassword.hexdigest()+"\n"



with open("shadow","r") as f:
    
    strings = f.read().split("\n")

    for i in strings:
        if(i.__contains__(args.username)):
            print("El usuario ya existe")
            exit()
            

with open("shadow","a") as f:
    f.write(line)
    

