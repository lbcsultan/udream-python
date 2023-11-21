from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_v1_5, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# 1. RSA 키 준비 (저장된 파일에서 읽어오기)
publicKey = RSA.import_key(open('publicKey.pem').read())
privateKey = RSA.import_key(open('privateKey.pem').read())
message = 'You can attack me 헬로월드'
print('평문:',message)

# 2. PKCS1_OAEP 
# 암호화 (송신자, 수신자의 공개키를 이용)
cipher = PKCS1_OAEP.new(publicKey)
ciphertext = cipher.encrypt(message.encode('utf-8'))
print('암호문:', ciphertext.hex())
# 복호화 (수신자, 수신자의 개인키를 이용)
decipher = PKCS1_OAEP.new(privateKey)
recovered = decipher.decrypt(ciphertext)
print('복호화평문:', recovered.decode('utf-8'))


