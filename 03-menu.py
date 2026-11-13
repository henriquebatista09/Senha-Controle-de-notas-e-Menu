def somar ():
    numero1 = float (input("digite um numero"))
    numero2 = float (input("digite um numero"))
    resultado = numero1 + numero2
    print (resultado)

def adicionar():
    numero1 = float (input("digite um numero"))
    numero2 = float (input("digite um numero"))
    resultado = numero1 - numero2
    print (resultado)

def multiplicar ():
    numero1 = float (input("digite um numero"))
    numero2 = float (input("digite um numero"))
    resultado = numero1 * numero2
    print (resultado)

def dividir ():
    numero1 = float (input("digite um numero"))
    numero2 = float (input("digite um numero"))
    resultado = numero1 / numero2
    print (resultado)

def pares ():
     quantidade = int(input("Digite quantos dos números pares você precisa"))
     contador = 0
     numero = 1
     while contador < quantidade:
           if numero % 2 == 0:
                 print(f"esses são os números: {numero}")
                 contador += 1
           numero += 1


def ímpares ():
     quantidade = int(input("Digite quantos dos números ímpares você precisa"))
     contador = 0
     numero = 1
     while contador < quantidade:
           if numero % 2 != 0:
                 print(f"esses são os números: {numero}")
                 contador += 1
           numero += 1





while True:
    print ("calculadora")
    print ("1 - adição")
    print ("2 - subtração")
    print ("3 - multiplicação")
    print ("4 - divisão")
    print ("5 - pares")
    print ("6 - impares")
    print ("7 - somatorio")
    print ("8 - atorial")

    print ("0 - sair")

    opcao = input ("Escolha uma opção:")
    if opcao == "1":
        somar()
    elif opcao == "2": 
        adicionar()
    elif opcao == "3":
        multiplicar()
    elif opcao == "4":
        dividir()
    elif opcao == "0":
        print ("saindo do sistema...")
        break
    elif opcao == "5":
        pares()
    elif opcao == "6":
         ímpares()
    else: 
        print ("opcao invalida, tente novamente!!!")
    