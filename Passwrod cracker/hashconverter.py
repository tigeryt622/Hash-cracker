import hashlib

password = "prince123"
hash_object = hashlib.sha256(password.encode())
print(hash_object.hexdigest())
