###### 5) Escreva um programa que inverta os caracteres de um string.
###### IMPORTANTE:
###### a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
###### b) Evite usar funções prontas, como, por exemplo, reverse;

###### PARA EXECUTAR O CÓDIGO: Digitar python exercicio5.py no terminal

###### Esse código foi desenvolvido com o auxílio de IA.

# Função para inverter uma string
def inverter_string(s):
    # Inicializa uma string vazia
    string_invertida = ""
    
    # Itera sobre a string original de trás para frente
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Exemplo de uso
entrada = input("Informe uma frase qualquer: ")  # Usuário informa a string
resultado = inverter_string(entrada)
print(f"Sua frase invertida: {resultado}")
