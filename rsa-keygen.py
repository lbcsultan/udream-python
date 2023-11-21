from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_v1_5, PKCS1_OAEP

# 1. RSA 키 생성 
key = RSA.generate(1024) 

# 2. RSA 키 내부 살펴보기 
# print('n=p.q=',key.n)
# print('p=',key.p)
# print('q=',key.q)
# print('e=',key.e)
# print('d=',key.d)

# 3. 키를 PEM 형식으로 변환하고 화면에 출력, 저장 
pri_key = key.export_key()
pub_key = key.publickey().export_key()
print('개인키:',pri_key)
print('공개키:',pub_key)

# 4. 키를 파일로 저장하기 
file_out = open('privateKey.pem', 'wb')
file_out.write(pri_key)
file_out.close()
file_out = open('publicKey.pem', 'wb')
file_out.write(pub_key)
file_out.close()

# 5. 개인키를 패스워드 암호화 저장 
secret_code = 'dkjlkdsjlskdjflkjsakjlghkjdslksdf'
encrypted_key = key.export_key(passphrase=secret_code,pkcs=8,protection='scryptAndAES128-CBC')
file_out = open('privateKeyEncrypted.pem', 'wb')
file_out.write(encrypted_key)
file_out.close() 

# 6. 패스워드 암호화된 개인키를 읽어오기 
encoded_key = open('privateKeyEncrypted.pem', 'rb').read() 
key1 = RSA.import_key(encoded_key, passphrase=secret_code)
pri_key1 = key1.export_key()
pub_key1 = key1.publickey().export_key()
print('읽어온 개인키:',pri_key1)
print('읽어온 공개키:',pub_key1)

# 7. 공개키 파일에서 공개키를 읽어오기 (외부인)
pub_key2 = open('publicKey.pem').read()
print('외부인이 가지고 있는 공개키:', pub_key2)

# 8. 암호화, 복호화에 사용할 개인키 
privateKey1 = RSA.import_key(pri_key1)
publicKey1 = RSA.import_key(pub_key1)
publicKey2 = RSA.import_key(pub_key2)