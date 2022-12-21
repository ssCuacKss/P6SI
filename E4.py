import argparse
from Crypto.Hash import SHA256, MD5

parser = argparse.ArgumentParser(description='compara dos hashes en MD5')

parser.add_argument("hashValue",help=" hash a comparar con entrada2", type=str)

parser.add_argument("entrada",help="texto a obtener su hash y comparar con hashValue", type=str)

args= parser.parse_args()

with open(args.entrada,"r") as f1:
    text = f1.read()


hash = MD5.new(bytes(text,'utf-8'))

print(args.hashValue)
print(hash.hexdigest())


if(args.hashValue != hash.hexdigest()):
    print("No tienen el mismo hash value")
else:
    print("tienen el mismo hash value")