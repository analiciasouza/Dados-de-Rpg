from random import randint
def dado(lados):
    valor = randint(1, lados)
    return valor



acao = ' '
while acao.lower() != 'sair':
    acao = input("Teste ou Dano? ")
    if acao.lower() == 'teste':
       lados_dado = int(input("Quantos lados tem o dado? "))
       numero_de_dados = int(input("Quantos dados vão ser usados? "))
       lista_valores = []
       for num in range(0, numero_de_dados):
            num = dado(lados_dado)
            lista_valores.append(num)
       print(lista_valores)
       print(f"Maior valor: {max(lista_valores)}")
    elif acao.lower() == 'dano':
       lados_dado = int(input("Quantos lados tem o dado? "))
       numero_de_dados = int(input("Quantos dados vão ser usados? "))
       lista_valores = []
       for num in range(0, numero_de_dados):
            num = dado(lados_dado)
            lista_valores.append(num)
       print(lista_valores)
       print(f"Soma: {sum(lista_valores)}")
    elif acao.lower() == 'sair':
       break
    else:
        print("Inválido")  


    




