import tkinter as tk

def clique_botao(event):
    #texto recebe um evento onde pode receber valores do tipo text
    texto=event.widget.cget("text")
    #se texto for "="
    if texto == "=":
     #tente
     try:
      #receber um valor ( valor.get() ), fazer o calculo inserido...(eval) e transoformar para str...pois a interface só aceita em strings
      resultado = str(eval(valor.get()))
      #resultado atualiza para o valor calculado
      valor.set(resultado)
      #terá exeções se
     except Exception as e:
      #valor der erro, irá escrever erro na tela
      valor.set("Erro")
      #se for C 
    elif texto == "C":
       valor.set("")#valor atualiza para vazio...apagando o que foi escrito
       #senão
    else:
       #atualiza o campo de entrada com o novo valor...
       valor.set(valor.get()+texto)

janela=tk.Tk()
janela.title("CALCULADORA")
janela.geometry("358x363")
janela.configure(bg="dark grey")

valor=tk.StringVar()#cria uma variável(logo abaixo) de texto que será usada para armazenar o valor do campo de entrada :
#recebe uma variavel de texto...com fontes de texto
entrada = tk.Entry(janela, textvar=valor, font="lucida 20 bold", bd=10, insertwidth=4, width=20, borderwidth=4 )
entrada.configure(bg="white",)
entrada.pack()#comando para funcionar

#botão recebe espaço na tela
botao_janela=tk.Frame(janela)
botao_janela.pack()#comando para funcionar
#botões da calculadora...
botoes=[
    '7 ','8 ','9 ','/ ','C',
    '4 ','5 ','6 ','* ','( ',
    '1 ','2 ','3 ','- ',') ',
    '0 ',' , ','=','+',      
    ]

linha=0
coluna=0

#para botao(variavel criada agora) em botoes:
for botao in botoes:
    #criasse um botão na tela para as teclas de botoes feitas acima com fontes de tamanhos de texto
    btn=tk.Button(botao_janela, text=botao, font= "lucida 15 bold", padx=20, pady=20)
    #começa da coluna 0 e linha 0
    btn.grid(row=linha,column=coluna)
    btn.bind("<Button-1>",clique_botao)
    btn.configure(bg="white")

    coluna+=1#a coluna vai andando de 1 em 1 
    #até 5...
    if coluna == 5:#quando chega em 5
        coluna=0#ela zera
        linha+=1#a linha anda 1
        #e começa uma nova coluna

janela.mainloop()
