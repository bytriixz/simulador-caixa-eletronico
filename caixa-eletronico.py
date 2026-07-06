import time
import random
import locale

locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')

print("Seja bem-vindo!")
time.sleep(2)

status = 0 
saldo = random.uniform(0, 10000) #gera um saldo aleatório

#loop de execução
while status == 0:
    
    #menu de funcionalidades
    print("\n----MENU----")
    print("1- Ver saldo")
    print("2- Saque")
    print("3- SAIR")
    print("------------\n")
    time.sleep(2)
    
    try:
        status = (int(input("Escolha uma opção: ")))
    
        
        if status ==1:  #Verificação de saldo
            print("Aguarde enquanto verificamos seu saldo.\n")
            time.sleep(3)
            print(f"Seu saldo atual é de: {locale.currency(saldo, symbol=True)}\n")#Formatação usando locale
            print("Retornando ao menu...")
            time.sleep(5)
            status +=-1
        
        elif status ==2: #Opção de saque
            print("Encaminhando para opção de saque. Aguarde.\n")
            time.sleep(3)
            #Informações adicionais
            print("Para saques acima de R$ 5.000 é necessário entrar em contato com sua agência para solicitar o agendamento e a reserva do dinheiro.")
            time.sleep(2)
            print("---------------------------------------------------")
            print("O caixa fornece notas de R$20, R$50, R$100 e R$200.")
            print("---------------------------------------------------\n")
            time.sleep(4)
            
            try:
                quantia = float(input(f"Digite a quantia que deseja sacar (Valor mínimo R$20,00): "))
                
                #Condição para saldo insuficiente
                if saldo < quantia : 
                    print("Saldo insufiente")
                    time.sleep(3)
                    print("Retornando ao menu...")
                    time.sleep(3)
                    status+=-2
                
                #Condição para valor abaixo do mínimo
                elif quantia <20:
                    print("Valor inválido. O valor mínimo é de R$20.")
                    time.sleep(3)
                    print("Retornando ao menu...")
                    time.sleep(3)
                    status +=-2
                
                #Condição para valor acima de 5000
                elif quantia > 5000:
                    print("Para saques acima de R$ 5.000 é necessário entrar em contato com sua agência para solicitar o agendamento e a reserva do dinheiro.\n")
                    print("Retornando ao menu... ")
                    time.sleep(8)
                    status=0
                
                #Verificação para notas disponíveis no caixa
                elif quantia%20 == 0 or quantia%50 == 0 or quantia%100 == 0 or quantia%200 == 0:
                    print(f"Valor escolhido: {locale.currency(quantia, symbol=True)}, aguarde a contagem das notas.\n")
                    time.sleep(5)
                    print("Retire as notas no contador.\n")
                    time.sleep(3)
                
                    print(f"Saldo anterior: {locale.currency(saldo, symbol=True)}")
                    saldo = saldo-quantia   
                    print(f"Saldo atual: {locale.currency(saldo, symbol=True)}\n")
                    time.sleep(4)
                
                    print("Retornando ao menu...")
                    time.sleep(5)
                    status +=-2
            
                #Condição para indisponibilidade de notas
                else:
                    print("Valor inválido. Digite apenas valores múltiplos das notas disponíveis.\n O caixa fornece notas de R$20, R$50, R$100 e R$200.")
                    time.sleep(3)
                    print("Retornando ao menu...")
                    time.sleep(3)
                    status +=-2
                
            except ValueError:
                print("Entrada inválida. Digite apenas números")
                time.sleep(3)
                status = 0
            
        elif status ==3:
            print("Esta função ainda não foi implementada.")
            print("Retornado ao menu...")
            time.sleep(3)
            status=0

        
        else:
            print("Entrada inválida. Digite apenas os números correspondentes às opções.")
            time.sleep(3)
            status +=-status 
        
    except ValueError:
        print("Entrada inválida. Digite apenas os números correspondentes às opções.")
        time.sleep(3)
        
        
    
        
    