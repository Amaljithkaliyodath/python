a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

while b != 0:
    c= a & b
    a = a ^ b
    b = c << 1

print(a)
