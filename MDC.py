print("Calcular o MDC. Digite dois números inteiros:")
a = int(input("a: "))
b = int(input("b: "))
c = a % b

while c != 0:
    a=b
    b=c
    c=a % b
 
print(b)