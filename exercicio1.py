"""
Exercício 1 – Identificando Quadrados Perfeitos

Objetivo:
Crie uma função chamada `classificar_quadrados` que receba uma lista de números inteiros e retorne um dicionário com duas chaves:
    - 'quadrados_perfeitos': contendo os números que são quadrados perfeitos (por exemplo, 1, 4, 9, 16, …);
    - 'nao_quadrados': contendo os demais números.

Requisitos:
- Utilize laços de repetição para percorrer a lista.
- Adicione uma docstring explicando o funcionamento da função.

Exemplo de chamada:
    resultado = classificar_quadrados([1, 2, 3, 4, 8, 9, 15])
    print(resultado)
    # Saída esperada: {'quadrados_perfeitos': [1, 4, 9], 'nao_quadrados': [2, 3, 8, 15]}
    
Importante:
- Não se preocupe com números negativos.
"""
# Sua solução aqui

def classificar_quadrados():
    num = []
    while True:
        try:
            entrada = input('Digite um numero para entrar na lista ou "finalizar" para verificar quais são quadrados: ')
            if entrada.lower == 'finalizar':
                break
            if not entrada.isdigit:
                print('Por favor, insira um numero válido ou "finalizar" para encerrar a inserção de numeros')
                num.append(int(entrada))
            if num % 2 == 0:
                print('o numero é um quadrado')
            else:
                print('o numero n é um quadrado')
        except ValueError:
            print('Insira um caractere valido')


classificar_quadrados()
            