###Escreva um programa que conta o número de vogais e consoantes em uma string.
algoritmo checklist:
- [] receber o texto para contar as vogais 
- [] percorrer o texto contando cada carctere 
- [] salvar a contagem de cada vogal  em um dicionario
- [] mostrar o resultado.
###

# Receber o texto para contar as vogais
texto = input("Digite um texto: ")
vogais_no _texto = {}

# Percorrer o texto contando cada caractere
for char in texto.lower():
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        if caracter in vogais_no_texto:
            vogais_no_texto[caracter] += 1
        else:
            vogais_no_texto[caracter] = 1'