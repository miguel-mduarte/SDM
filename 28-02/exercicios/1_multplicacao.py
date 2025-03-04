# Faça um algoritmo que calcule a multiplicação entre dois números sem utilizar o sinal de multiplicação ( * ) 
# ou função. Utilize estrutura de repetição e soma.

n = int(input("Digite um número: "))
m = int(input("Digite outro número: "))
r = n
for i in range(1, m):
    r += n
print(r)