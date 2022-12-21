import argparse
from Crypto.Hash import SHA256, MD5

parser = argparse.ArgumentParser(description='obtine el hash un fichero de texto en SHA256')

parser.add_argument("entrada",help="el nombre del fichero a encriptar", type=str)

args= parser.parse_args()

with open(args.entrada,"r") as f:
    text = f.read()


hash = SHA256.new(bytes(text,'utf-8'))

print(hash.hexdigest())
