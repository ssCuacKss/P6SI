from Crypto.Hash import SHA256, MD5

hash_objectA = MD5.new(b'First')
hash_objectB = MD5.new(b'first')

print("'First' chain hash MD5")
print(hash_objectA.hexdigest())
print(hash_objectA.digest_size)
print(hash_objectA.block_size)

print("'first' chain hash MD5")
print(hash_objectB.hexdigest())
print(hash_objectB.digest_size)
print(hash_objectB.block_size)