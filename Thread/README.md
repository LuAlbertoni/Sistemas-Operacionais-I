## Exercício: Cálculo de Fatoriais com Threads

Este repositório contém dois programas em Python que calculam fatoriais: `cálculoFatorial.py` e `thread.py`. A seguir, descrevemos o exercício que esses programas resolvem:

### Enunciado do Exercício

Elaborar um programa em Python ou C# que calcule vários números fatoriais:

- O programa deve inicialmente perguntar ao usuário a quantidade de cálculos a serem realizados;
- Para cada cálculo o programa deve perguntar ao usuário um número;
- Em seguida, o programa deve iniciar uma thread para cada cálculo, calculando os respectivos fatoriais dos números informados;
- Cada thread deve ter um nome único e deve exibir seu nome junto com a iteração no cálculo do fatorial, mostrando a iteração e o cálculo da iteração. Ao final do cálculo, exibir o resultado do fatorial.

Exemplo de uma thread calculando o fatorial de 5:

Thread 3 - Iniciou
Thread 3 - 5 (cálculo iteração: 5)
Thread 3 - 4 (cálculo iteração: 20)
Thread 3 - 3 (cálculo iteração: 60)
Thread 3 - 2 (cálculo iteração: 120)
Thread 3 - Resultado 120

### Arquivos de Código

- O arquivo `cálculoFatorial.py` contém um código que calcula o fatorial de forma sequencial. Isso significa que ele calcula o fatorial de um número antes de passar para o próximo.
- Já o arquivo `thread.py` utiliza a biblioteca padrão do Python chamada 'threading', que proporciona meios para criar e gerenciar threads. Este código utiliza threads para calcular o fatorial de forma paralela.