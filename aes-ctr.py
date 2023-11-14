import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad 

# 암호화 
data = 'Secret message 보안 정보'.encode('utf-8') 
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(pad(data,AES.block_size))
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'nonce': nonce, 'ciphertext': ct})
print("비밀키: ", key.hex())
print("암호문: ", result)

# 복호화 
try:
 b64 = json.loads(result)
 nonce = b64decode(b64['nonce'])
 ct = b64decode(b64['ciphertext'])
 cipher = AES.new(key, AES.MODE_CTR, nonce=nonce) 
 pt = unpad(cipher.decrypt(ct),AES.block_size).decode('utf-8')
 print("The message was: ", pt)
except ValueError as KeyError:
 print("Incorrect decryption") 
