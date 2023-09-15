# Função para calcular o fatorial de um número e exibir os passos de cálculo
def calculoFatorial(num, nomeThread):
    result = 1
    
    print(f"Thread {nomeThread} - Iniciou")
    
    for i in range(num, 0, -1):  # Inverte o loop para ordem decrescente
        result *= i
        
        if i != 1:
            print(f"Thread {nomeThread} - {i} (cálculo iteração: {result})")
            
    print(f"Thread {nomeThread} - Resultado {result}")

def main():
    # Solicitar ao usuário a quantidade de cálculos a serem realizados
    qntCalculos = int(input("Digite a quantidade de cálculos a serem realizados: "))

    # Para cada cálculo, solicitar o número e realizar o cálculo sequencialmente
    for i in range(qntCalculos):
        num = int(input(f"Digite o número para o cálculo {i + 1}: "))
        
        nomeThread = f"{i + 1}"
        
        calculoFatorial(num, nomeThread)

main()
