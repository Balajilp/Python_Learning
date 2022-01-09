a = input()
b = ord(a[0])+ord(a[1])+ord(a[2])+ord(a[3])
def mul(m, n):
    return 1 if m%n == 0  else 0
print(mul(b, 8))