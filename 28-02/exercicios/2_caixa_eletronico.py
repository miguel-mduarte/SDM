# Faça um algoritmo com as funções de um caixa eletrônico. Utilize estrutura de repetição. 
# - Deve apresentar um menu:
# 1 - Saldo
# 2 - Saque
# 3 - Depósito
# 4 - Sair
# - O algoritmo deve executar as operações de um cliente até que ele digite a opção 4- Sair.
# - Caso o cliente digite uma opção que não exista informe "Opção inválida".
# - Algoritmo deve operar as quatro funções do caixa eletrônico.
# - O Saldo inicial é igual a 0,00.
# - Caso o usuário tente sacar um valor maior que o saldo disponível o programa deve apresentar a mensagem 
# "Saldo insuficiente".
# - No final de cada operação o saldo deve ser apresentado.

saldo = 0
opcao = int(input("------------------------------------------------\n",
                 "1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Sair\n"
                 "------------------------------------------------\n"))

while 0<opcao<4:
    if opcao == 1:
        deposito = int(input("Quanto voce quer depositar?"))
        saldo += deposito
        print(f"Seu deposito foi um sucesso!\nSaldo Atual: {saldo}")
        opcao = int(input("------------------------------------------------\n",
                         "1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Sair\n"
                         "------------------------------------------------\n"))    
    elif opcao == 2:
        saque = int(input("Quanto voce quer sacar?"))
        if saldo > saque:
            saldo -= saque
            print(f"seu saque foi um sucesso!\nSaldo Atual: {saldo}")
            opcao = int(input("------------------------------------------------\n",
                            "1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Sair\n"
                            "------------------------------------------------\n"))
        else:
            print(f"saldo insuficiente.\nSaldo atual: {saldo}")
            opcao = int(input("------------------------------------------------\n",
                            "1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Sair\n"
                            "------------------------------------------------\n"))
    elif opcao == 3:
        print(f"Saldo atual: {saldo}")
        opcao = int(input("------------------------------------------------\n",
                        "1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Sair\n"
                        "------------------------------------------------\n"))
        
if opcao == 4: 
    print("Volte sempre!")
else: 
    print("Opção inválida.\n") 
    opcao = int(input("------------------------------------------------\n",
                        "1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Sair\n"
                        "------------------------------------------------\n"))




