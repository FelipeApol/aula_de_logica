'''Contar palavras em uma frase
Escreva um programa que conta o número de palavras em uma frase.

[] - Receber a frase do usuário
[] - contar o número de palavras na frase
[] - mostrar o resultado
 '''
frase = input("Digite uma frase: ")
palavras = frase.split()
print(f"O número de palavras na frase é: {len(palavras)}")  
