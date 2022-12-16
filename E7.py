
from Crypto.Hash import HMAC,SHA256



hash1 = HMAC.new(b'12345',b'yoo!, Its rewind time',digestmod=SHA256)
hash2 = HMAC.new(b'1234',b'yoo!, Its rewind time',digestmod=SHA256)
hash3 = HMAC.new(b'12345',b'yo!, Its rewind time',digestmod=SHA256)


print("encriptacion sin cambiar nada")
print(hash1.hexdigest())
print("encriptacion cambiando la key")
print(hash2.hexdigest())
print("encriptacion cambiando un caracter del mensaje")
print(hash3.hexdigest())

