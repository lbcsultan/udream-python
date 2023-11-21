from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


# 1. 송신자 
data = "I met aliens in UFO. Here is the map. 내가 ET를 만났다구."
print('입력 평문:', data)
file_out = open("encrypted_data.bin", "wb")
recipient_key = RSA.import_key(open("publicKey.pem").read())
# AES 암호화를 위한 난수키 생성
session_key = get_random_bytes(16) 
print('세션키:', session_key.hex())
# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)
print('암호화된세션키:', enc_session_key.hex())
# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data.encode("utf-8"))
[file_out.write(x)
  for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
file_out.close()
print('암호문:', ciphertext.hex())
print('tag:', tag.hex())
print('nonce:', cipher_aes.nonce.hex())
print() 

# 2. 수신자  
file_in = open("encrypted_data.bin", "rb")
private_key = RSA.import_key(open("privateKey.pem").read())
enc_session_key, nonce, tag, ciphertext = \
[file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)] 
# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)
print('복구된세션키:', session_key.hex())
# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print('출력 평문:',data.decode("utf-8"))
