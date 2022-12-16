import argparse
from Crypto.Hash import SHA256, MD5

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en MD5')

parser.add_argument("hashValue",help="el nombre del fichero a encriptar y comparar con entrada2", type=str)

parser.add_argument("entrada",help="el nombre del fichero a encriptar y comparar con entrada", type=str)

args= parser.parse_args()

with open(args.entrada,"r") as f1:
    text = f1.read()


hash = SHA256.new(bytes(text,'utf-8'))

print(args.hashValue)
print(hash.hexdigest())


if(args.hashValue != hash.hexdigest()):
    print("No tienen el mismo hash value")
else:
    print("tienen el mismo hash value")