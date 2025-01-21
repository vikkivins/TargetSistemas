###### 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
###### sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
###### escreva um programa na linguagem que desejar onde, informado um número, ele 
###### calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número 
###### informado pertence ou não a sequência.

###### PARA EXECUTAR O CÓDIGO: Digitar python exercicio2.py no terminal

###### Esse código foi desenvolvido com o auxílio de IA.

def sequencia_fibonacci(limit):
    sequencia_fib = [0, 1]  # Inicializa a sequência com os dois primeiros números
    while sequencia_fib[-1] < limit:
        sequencia_fib.append(sequencia_fib[-1] + sequencia_fib[-2])  # Calcula o próximo número
    return sequencia_fib

def eh_fibonacci(number):
    sequence = sequencia_fibonacci(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} NÃO pertence à sequência de Fibonacci."

# Entrada do usuário
num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
print(eh_fibonacci(num))
