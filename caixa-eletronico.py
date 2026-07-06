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
    
        
        if status ==1:
            print("Aguarde enquanto verificamos seu saldo.\n")
            time.sleep(3)
            print(f"Seu saldo atual é de: {locale.currency(saldo, symbol=True)}\n")
            print("Retornando ao menu...")
            time.sleep(5)
            status +=-1
        
        elif status ==2:
            print("Esta função ainda não foi implementada.")
            print("Retornado ao menu...")
            time.sleep(3)
            status=0
            
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
        
        
    
        
    