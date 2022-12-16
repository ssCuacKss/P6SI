import argparse
from Crypto.Hash import SHA256, MD5

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en MD5')

parser.add_argument("entrada",help="el nombre del fichero a encriptar y comparar con entrada2", type=str)

parser.add_argument("entrada2",help="el nombre del fichero a encriptar y comparar con entrada", type=str)

args= parser.parse_args()

with open(args.entrada,"r") as f1:
    text = f1.read()

with open(args.entrada2,"r") as f2:
    text1 = f2.read()


hash1 = SHA256.new(bytes(text,'utf-8'))
hash2 = SHA256.new(bytes(text1,'utf-8'))

print(hash1.hexdigest())
print(hash2.hexdigest())


if(hash1.hexdigest() != hash2.hexdigest()):
    print("No tienen el mismo hash value")
else:
    print("tienen el mismo hash value")