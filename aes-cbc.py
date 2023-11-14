import json
from base64 import b64encode, b64decode 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad 
from Crypto.Random import get_random_bytes

# 암호화 (송신자)
data = 'Secret message 보안 정보'.encode('utf-8') 
key = get_random_bytes(32) # 128->16, 192->24, 256->32
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data,AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8') 
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct}) 
print('비밀키:', key.hex())
print('암호문:',result) 

# 복호화 (수신자)
try:
  b64 = json.loads(result)
  iv = b64decode(b64['iv'])
  ct = b64decode(b64['ciphertext'])
  decipher = AES.new(key, AES.MODE_CBC, iv)
  pt = unpad(decipher.decrypt(ct),AES.block_size).decode('utf-8')
  print('복호화 평문:',pt)
except ValueError as KeyError:
  print('Incorrect decryption')