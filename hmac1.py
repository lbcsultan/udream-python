from Crypto.Hash import HMAC, SHA256, SHA512 

# 송신자 - HMAC 계산 
secret = b'secret'
message = b'Message'
h = HMAC.new(secret, digestmod=SHA512)
h.update(message)
hmac = h.hexdigest()
print(hmac)

# 송신자가 수신자에게 <message, hmac>을 전송합니다.

# 수신자 - HMAC 검증
secret = b'secret'
message = b'Message'
h = HMAC.new(secret, digestmod=SHA512)
h.update(message)
try:
  h.hexverify(hmac)
  print('메시지가 유효합니다.')
except ValueError:
  print("잘못된 메시지입니다.")
