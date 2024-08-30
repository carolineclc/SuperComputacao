#include <iostream>
#include <vector>
#include <algorithm>

// Função recursiva para resolver o problema da mochila
int knapsack(int capacity, const std::vector<int>& weights, const std::vector<int>& values, int n) {
    // Caso base: se não há mais itens ou a capacidade da mochila é 0
    if (n == 0 || capacity == 0) {
        return 0;
    }

    // Se o peso do n-ésimo item é maior que a capacidade da mochila, não podemos incluí-lo
    if (weights[n-1] > capacity) {
        return knapsack(capacity, weights, values, n-1);
    } else {
        // Caso contrário, temos duas opções: incluir ou não incluir o n-ésimo item
        int includeItem = values[n-1] + knapsack(capacity - weights[n-1], weights, values, n-1);
        int excludeItem = knapsack(capacity, weights, values, n-1);

        // Retorna o máximo valor entre as duas opções
        return std::max(includeItem, excludeItem);
    }
}

int main() {
    // Exemplo de entrada: pesos e valores dos itens
    std::vector<int> weights = {1,1,2,1,8};
    std::vector<int> values = {5,10,5,20,25};
    int capacity = 10;

    int n = weights.size();

    // Chama a função knapsack e exibe o resultado
    int max_value = knapsack(capacity, weights, values, n);
    std::cout << "Valor máximo que pode ser colocado na mochila: " << max_value << std::endl;

    return 0;
}

