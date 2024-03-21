def inverte_string(string):
    # Inicializa uma string vazia para armazenar o resultado invertido
    string_invertida = ""

    # Itera sobre os caracteres da string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        # Adiciona cada caractere à string invertida
        string_invertida += string[i]

    # Retorna a string invertida
    return string_invertida

# Exemplo de uso
string_original = "Hello, world!"
string_invertida = inverte_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)