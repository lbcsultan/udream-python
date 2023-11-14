from base64 import b64encode, b64decode

p = "Hello 헬로" 

#String <--> byte 
print('string:',p)
utf8 = p.encode('utf-8')
print('UTF-8:',utf8) 
p1 = utf8.decode('utf-8')
print('string1:',p1)

# byte <--> base64
print('byte <--> base64')
print('byte: ', utf8)
b64 = b64encode(utf8)
print('base64: ', b64)
b64d = b64decode(b64)
print('byte: ', b64d)
print()
