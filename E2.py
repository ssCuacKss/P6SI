import argparse
from Crypto.Hash import SHA256, MD5

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en MD5')

parser.add_argument("entrada",help="el nombre del fichero a encriptar", type=str)

args= parser.parse_args()

with open(args.entrada,"r") as f:
    text = f.read()


binstr = bytearray(text, encoding='utf-8')

hash = MD5.new(binstr)

print(hash.hexdigest())
