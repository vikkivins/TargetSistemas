###### 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
###### • O menor valor de faturamento ocorrido em um dia do mês;
###### • O maior valor de faturamento ocorrido em um dia do mês;
###### • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

###### IMPORTANTE:
###### a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
###### b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

###### PARA EXECUTAR O CÓDIGO: Digitar python exercicio3.py no terminal. 
###### ATENÇÃO: O arquivo faturamento.json precisa estar JUNTO com o arquivo exercicio3.py no mesmo local.

###### Esse código foi desenvolvido com o auxílio de IA.

import json

def analisar_faturamento(arquivo_json):
    # Carregar dados do JSON
    with open(arquivo_json, "r") as file:
        dados = json.load(file)
    
    # Extrair apenas os valores de faturamento
    faturamento_diario = [dia["valor"] for dia in dados]

    # Ignorar dias sem faturamento (valores iguais a 0)
    faturamento_valido = [valor for valor in faturamento_diario if valor > 0]

    # Calcular menor e maior valor de faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    # Calcular a média mensal (considerando apenas dias com faturamento)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Contar dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    # Exibir resultados
    print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
    print(f"Média de faturamento mensal: R$ {media_mensal:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Nome do arquivo JSON
arquivo = "faturamento.json"

# Executar análise
analisar_faturamento(arquivo)