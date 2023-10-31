print('곱셈테이블 출력')
p = 10
for x in range(0, p):
  print(f'-------', end='\t')
print()
print(f'| X', end='\t')
for x in range(1, p):
  print(f'| {x}', end='\t')
print()
for x in range(0, p):
  print(f'-------', end='\t')
print()
for x in range(1, p):
  print(f'| {x}', end='\t')
  for y in range(1, p):
    print(f'| {x * y}', end='\t')
  print()
for x in range(0, p):
  print(f'-------', end='\t')
print()