import threading

# Função para calcular o fatorial de um número e exibir os passos de cálculo
def calculoFatorial(num, nomeThread, results):
    print(f"Thread {nomeThread} - Iniciou")
    
    result = 1
    
    for i in range(num, 0, -1):
        result *= i
        
        if i != 1:
            print(f"Thread {nomeThread} - {i} (cálculo iteração: {result})")
            
    print(f"Thread {nomeThread} - Resultado {result}")
    
    results[nomeThread] = result

def main():
    threads = []
    results = {}
    valores = []
    
    # Solicitar ao usuário a quantidade de cálculos a serem realizados
    quantCalculos = int(input("Digite a quantidade de cálculos a serem realizados: "))

    # Solicitar os números e armazená-los em uma lista
    for i in range(quantCalculos):
        num = int(input(f"Digite o número para o cálculo {i + 1}: "))
        valores.append(num)

    # Iniciar uma thread para cada cálculo do fatorial
    for i, num in enumerate(valores):
        nomeThread = i + 1
        thread = threading.Thread(target=calculoFatorial, args=(num, nomeThread, results))
        threads.append(thread)
        thread.start()

    # Aguardar que todas as threads terminem antes de encerrar o programa
    for thread in threads:
        thread.join()

    # Exibir todos os resultados no final
    print("\nResultados dos cálculos de fatorial:")
    
    for nomeThread, result in results.items():
        print(f"Thread {nomeThread}: {result}")

main()