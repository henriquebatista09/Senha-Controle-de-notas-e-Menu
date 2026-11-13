nome_digitado= input("digite seu nome:")
uma_nota = float (input("digite uma nota"))
adicionar = input("deseja adicionar outra nota?")
nota2 =  float(input("Digite sua outra nota: "))

if adicionar == "não" or adicionar == "nao":

    print(nome_digitado) 
    print(uma_nota)
    if uma_nota >= 5:
        print("Aprovado!")
    if uma_nota < 5:
        print("Reprovado!")

if adicionar == "sim":
        print(nota2)



    



