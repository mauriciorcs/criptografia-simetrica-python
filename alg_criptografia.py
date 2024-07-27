# Alfabetos minusculos e maiusculos: define dois conjuntos de caracteres, um para letras minúsculas e outro para letras maiusculas.
# Iteração pela mensagem: para cada caractere na mensagem, verifica se é uma letra minúscula ou maiúscula.

# alf.index(i): encontra o índice do caractere i no alfabeto estendido alf.
# + key: Adiciona a chave de criptografia ao índice encontrado.
# % len(alf): Aplica o operador módulo (%) ao resultado da soma para garantir que o índice resultante esteja dentro dos limites do alfabeto estendido.



def encryption(msg, key):
    alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!@# "
    encoded = ""

    for i in msg:
        if i in alf:           # Para cada caractere na mensagem (msg), verifica se está no alfabeto (alf).
            numeroEconde = (alf.index(i) + key) % len(alf)   # Calcula a nova posição do caractere criptografado: (alf.index(i) + key) % len(alf).
            encoded += alf[numeroEconde]   # Adiciona o caractere criptografado ao resultado (encoded).
        else:
            encoded += i  # Caractere não reconhecido, adicionado diretamente

    return encoded


def decryption(crypto, key):
    alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!@# "
    decoded = ""

    for i in crypto:
        if i in alf:
            numeroDeconded = (alf.index(i) - key + len(alf)) % len(alf)
            decoded += alf[numeroDeconded]
        else:
            decoded += i  # Caractere não reconhecido, adicionado diretamente

    return decoded


msg = input("Digite a mensagem que deseja encriptar: ")
key = int(input("Digite a chave de criptografia (um número inteiro): "))

encriptacao = encryption(msg, key)
print("Texto encriptado:", encriptacao)

opcao = input("Deseja descriptografar a mensagem? (s/n): ")
if opcao.lower() == 's':
    decriptacao = decryption(encriptacao, key)
    print("Texto decriptado:", decriptacao)
else:
    print("A mensagem não foi descriptografada.")