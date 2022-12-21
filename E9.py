import argparse
from Crypto.Hash import SHA256, HMAC

parser = argparse.ArgumentParser(description='obtiene el hash un fichor de texto en HMAC')

parser.add_argument("mensaje",help="mensaje a encriptar", type=str)

parser.add_argument("key",help="clave del fichero a encriptar", type=str)

args= parser.parse_args()

with open(args.entrada,"r") as f1:
    text = f1.read()


hash = HMAC.new(bytes(args.key,'utf-8'),bytes(text,'utf-8'),digestmod=SHA256)

print(hash.hexdigest())

