def fibonacci(numero):
    fibonacci_ant = 0
    fibonacci_atual = 1
    
    while fibonacci_atual <= numero:
        if fibonacci_atual == numero:
            return True
        fibonacci_prox = fibonacci_ant + fibonacci_atual
        fibonacci_ant = fibonacci_atual
        fibonacci_atual = fibonacci_prox
    
    return False

# Função para verificar se um número pertence à sequência de Fibonacci
def verifica_fibonacci(numero):
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Teste
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
verifica_fibonacci(numero)