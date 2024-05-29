import string
import random

#Atualização....

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

3.
def forca_da_senha(senha):#Verifica a força da senha
    comprimento=len(senha)
    tem_maiusculas=any(c.isupper()for c in senha)#Verifica se tem alguma letra maiuscula na senha
    tem_minusculas=any(c.islower()for c in senha)#verifica se tem alguma letra minuscula na senha
    tem_numero=any(c.isdigit() for c in senha)#verifica se tem algum numero na senha
    tem_especiais=any(c in string.punctuation for c in senha)#verifica se tem algum caractere na senha

    criterios=sum([tem_maiusculas,tem_minusculas,tem_numero,tem_especiais])#soma todos os criterios aceitos (letras maiusculas e minusculas) numero e carectere especial
    if comprimento >=12 and criterios>=3:#se o comprimento da senha for maior ou igual a 12 e os criterios(ou seja, a quantidade de criterios que foi aceito na geração da senha) retorna um feedback
        return "Muito Forte"
    elif comprimento >=8 and criterios>=2:
        return "Forte"
    elif comprimento >=6:
        return "Moderada"
    else:
        return "Fraca"
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
#1
    #Gerar senha com os parametros escolhidos.
    senha = gerar_senha(comprimento,letras_maiusculas,letras_maiusculas,numeros,caracteres_especiais)
    
    #Recebe feedback
    seguranca = forca_da_senha(senha)
#4
    print("Senha gerada: ",senha)
    print(f"A segurança da senha é {seguranca}")
    
if __name__ == "__main__":
    main()