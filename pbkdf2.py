from Crypto.Protocol.KDF import PBKDF2 
from Crypto.Hash import SHA256 
from Crypto.Random import get_random_bytes 

password = b'gffdjklghjdhhhfjkd'
salt = get_random_bytes(16)
keys = PBKDF2(password, salt, 64, count=1000, hmac_hash_module=SHA256) 

print('Password:', password)
print('Salt:', salt.hex())
print('Key:', keys.hex())