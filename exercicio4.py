"""
Exercício 4 – Debugging Avançado com map, filter e reduce

Objetivo:
O código a seguir tem a intenção de:
    1. Solicitar ao usuário uma lista de números separados por vírgula.
    2. Converter essa entrada em uma lista de inteiros.
    3. Utilizar a função map para calcular o quadrado de cada número.
    4. Utilizar a função filter para selecionar apenas os quadrados que são pares.
    5. Utilizar a função reduce para somar todos os quadrados pares.
    6. Calcular e exibir a média dos quadrados pares (esta parte está ausente e deve ser implementada).


Contudo, o código apresenta diversos erros que impedem sua execução correta.

Tarefas:
    - Identifique e corrija os erros de conversão de tipos, sintaxe e lógica presentes.
    - Adicione 2 ou 3 linhas de código para calcular a média dos quadrados pares e exiba esse resultado.
    - Insira comentários explicando as correções e as novas linhas adicionadas.


Código com erros:
--------------------------------------------------

numbers_input = input("Digite uma lista de números separados por vírgula: ")

# O código a seguir tenta processar a entrada do usuário,
# mas não converte os elementos para inteiros.
numbers_list = numbers_input.split(",")

squared_numbers = map(lambda x: x ** 2, numbers_list)

even_numbers = filter(x % 2 == 0, squared_numbers)

total = functools.reduce(lambda x, y: x + y) even_numbers

print "Soma dos quadrados pares:", total
--------------------------------------------------

Após corrigir os erros e adicionar as linhas para calcular a média, o programa deverá:
    - Exibir a soma dos quadrados pares.
    - Exibir a média dos quadrados pares (soma dividida pelo número de elementos filtrados).

Boa sorte e bons estudos!
"""

# O aluno deve realizar as correções e implementações necessárias abaixo.

#vamos chamar o dicionario para importar o reduce
from functools import reduce

#Agora vamos criar uma funçaõ para que o codigo ocorra de forma correta
def num_quadrados():
    #criar uma lista para onde os valores inteiros vão ficar guardados
    num = []
    #laço de repetição para que seja colocados quantos numeros o usuario quiser
    while True:
        #try e except para não finalizar o sistema caso dê algo errado
        try:
            #tem como função adicionar numeros inteiros à lista e possui a função "000" que serve para parar de adicionar numeros à lista
            numeros = int(input('Digite um numero para entrar na lista ou "000" para parar o sistema e verificar quais são quadrados: '))
            #para a lista para que os calculos comecem
            if numeros == '000':
                break
            #adiciona os valores de numeros à lista
            num.append(numeros)
        except ValueError:
            print('Insira um caractere valido')
            
    #trocar "numbers_input.split" pela lista criada
    numbers_list = num(",")
    #adição do 'list' para chamar a lista e o map operar
    squared_numbers = list(map(lambda x: x ** 2, numbers_list))
                    #adcionamos 'list' e lambda
    even_numbers = list(filter(lambda x: x % 2 == 0, squared_numbers))
    #soma os valores dos numeros quadrados
            #deixamos só o reduce      #colocamos o "even_numbers" dentro dos () para funcionar
    total = reduce(lambda x, y: x + y, even_numbers)
    #adicionar () no print, f para a ser possivel printar o total e {} no total para o total ser printado 
    print(f"Soma dos quadrados pares:, {total}")
    
    #pega o valor da soma e divide pela quantidade de intens da lista de numeros quadrados
    media = map(lambda x: x % len(squared_numbers), total)
    print(f'a media da soma dos numeros quadrados pares é {media}')
    
#acionar a função para ela operar
num_quadrados()