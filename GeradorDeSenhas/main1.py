import string
import random

2.
def gerar_senha(comprimento,letras_maiusculas=True,letras_minusculas=True,numeros=True,caracteres_especiais=True):
    #Recebe todos caracteres se escolhidos
    caracteres = ""
    #Se parametro letras maiúsculas for escolhido, caracteres recebe de A até z maiúsculas
    if letras_maiusculas:
        caracteres += string.ascii_uppercase
    #Se parametro letras minúsculas for escolhido, caracteres recebe de a até z minúsculas
    if letras_minusculas:
        caracteres += string.ascii_lowercase
    #Se parametro numeros for escolhido, caracteres recebe de 1 até 9:
    if numeros:
        caracteres += string.digits
    #Se parametro caracteres epeciais for escolhido, caracteres recebe ,.!^:;.....
    if caracteres_especiais:
        caracteres += string.punctuation
    
#2.   
    #senha junta de acordo com o comprimento
    #aleatóriamente (se True) todas letras(maiúsculas,minúsculas) números e caracteres especiais
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    #Retorna a senha gerada
#3
    return senha
   
1.
def main():
    #Comprimento da senha
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    #Aceita letras maiúsculas
    letras_maiusculas = input("Deseja incluir letras maiúsculas ? (sim/não): ").lower() == "sim"
    #Aceita letras minúsculas
    letras_minusculas = input("Deseja incluir letras minúsculas ? (sim/não): ").lower() == "sim"
    #Aceita números
    numeros = input("Deseja incluir números ? (sim/não): ").lower() == "sim"
    #Aceita caracteres especiais
    caracteres_especiais = input("Deseja incluir caracteres especiais ? (sim/não) :").lower() == "sim"
    #Gerar senha com os parametros escolhidos.
#1.
    senha = gerar_senha(comprimento,letras_maiusculas,letras_maiusculas,numeros,caracteres_especiais)
    #Mostrar senha gerada
#4
    print("Senha gerada: ",senha)

if __name__ == "__main__":
    main()