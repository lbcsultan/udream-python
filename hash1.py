from Crypto.Hash import SHA256, SHA224, SHA384, SHA512

message = '한글메시지'
message_byte = bytearray(message, 'utf8')

h = SHA224.new()  
h.update(message.encode('utf8'))
print('SHA224:',h.hexdigest())
print()

h = SHA256.new() 
h.update(message.encode('utf8'))
print('SHA256:',h.hexdigest())
print()

h = SHA384.new() 
h.update(message.encode('utf8'))
print('SHA384:',h.hexdigest())
print()

h = SHA512.new() 
h.update(message.encode('utf8'))
print('SHA512:',h.hexdigest())