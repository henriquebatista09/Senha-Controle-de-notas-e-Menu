nome_digitado= input("digite o nome:")
senha_digitada = input ("digite sua senha:")
senha_cadastrada = '123'
nome_cadastrado = 'ana'
while senha_digitada != senha_cadastrada or nome_cadastrado != nome_digitado:
    print ("senha ou nome incorreta! Tente novamente.")
    nome_cadastrado = input("digite seu nome:")
    senha_digitada = input("digite sua senha:")

print (f"{nome_digitado} bem-vindo ao sistema...")