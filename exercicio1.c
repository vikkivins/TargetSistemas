// 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
// Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
// Imprimir(SOMA);
// Ao final do processamento, qual será o valor da variável SOMA?

// RESPOSTA: O resultado final é 91
// Para executar o código, existe a opção de utilizar o mycompiler.io para código C

// Esse código foi desenvolvido com o auxílio de IA.


#include <stdio.h>

int main() {
    int INDICE = 13, SOMA = 0, K = 0;

    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }

    printf("O valor final de SOMA é: %d\n", SOMA);

    return 0;
}

//MOSTRANDO TODAS AS SOMAS DE ACORDO COM A ITERAÇÃO
//ATENÇÃO: Utilizar somente um dos dois códigos para fazer o teste.

//#include <stdio.h>

//int main() {
//    int INDICE = 13, SOMA = 0, K = 0;

//    printf("Iteracao | K Atual | SOMA Atual\n");
//   printf("-------------------------------\n");

//    while (K < INDICE) {
//        K = K + 1;
//        SOMA = SOMA + K;
//        printf("%8d | %7d | %10d\n", K, K, SOMA); // Mostra os valores de K e SOMA
//    }

//    printf("\nO valor final de SOMA é: %d\n", SOMA);

//    return 0;
//}
