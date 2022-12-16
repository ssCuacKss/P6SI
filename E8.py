import argparse
from Crypto.Hash import SHA256, HMAC

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en MD5')

parser.add_argument("mensaje",help="el nombre del fichero a encriptar y comparar con entrada2", type=str)

parser.add_argument("key",help="el nombre del fichero a encriptar y comparar con entrada2", type=str)


args= parser.parse_args()

hash = HMAC.new(bytes(args.key,'utf-8'),bytes(args.mensaje,'utf-8'),digestmod=SHA256)

print(hash.hexdigest())

