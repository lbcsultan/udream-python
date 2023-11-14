from base64 import b64encode
from Crypto.Hash import SHA256 
from Crypto.Protocol.KDF import bcrypt, bcrypt_check 

# 1. 사용자 등록: Password Hash 생성 
password=b'test'
b64pwd = b64encode(SHA256.new(password).digest())
bcrypt_hash = bcrypt(b64pwd, 12) 
print('Password:', password)
print('b64pwd:', b64pwd)
print('PasswordHash:', bcrypt_hash)

# 2. 사용자 로그인: password hash 검증 
password_to_test = b'test1'
print('Password to test:', password_to_test)
try: 
  b64pwd1 = b64encode(SHA256.new(password_to_test).digest())
  bcrypt_check(b64pwd1, bcrypt_hash)
  print('로그인 성공')
except ValueError:
  print('로그인 실패!!!!!')