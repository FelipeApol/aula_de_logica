'''
Escreva um programa que conta o número de vogais e consoantes em uma string.
algoritmo checklist:
-[] receber o texto para contar as vogais 
-[] percorrer o texto contando cada carctere 
-[] salvar a contagem de cada vogal  em um dicionario
-[] mostrar o resultado.
'''

# Receber o texto para contar as vogais
texto = input("Digite um texto: ")
vogais_no_texto = 0 
consoantes_no_texto = 0 


# Percorrer o texto contando cada caractere
for caractere in texto:
    if caractere in 'aeiouAEIOU':
        vogais_no_texto += 1
    else:
        consoantes_no_texto += 1

# Mostrar o resultado
print(f"Vogais: {vogais_no_texto}")
print(f"Consoantes: {consoantes_no_texto}")