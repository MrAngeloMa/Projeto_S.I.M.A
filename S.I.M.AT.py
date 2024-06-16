# S.I.M.A
from tkinter import *
from EstruturaT import *

############################### Estrutura do Programa ################################

########################### Iniciando o programa ###########################

# Inicia a função que define os parâmetros das salas
TBots, TMapas, TSalas = CriaMapa(player) 

########################  Interface ############################

# Define a função que determina a ação do botão quando o usuário clica nele
# Quando o usuário clica no botão, a função Estrutura() é chamada e inicia a simulação
def chamarbotao():
    Estrutura(TMapas, TBots, TSalas, player)

# Define a função que cria a interface do programa
def Interface():

    # Criando janela e importando imagem de fundo
    janela = Tk()
    img = PhotoImage(file="Imagens/Projeto.png")

    # Definindo parâmetros da janela
    janela.geometry("1300x700")
    janela.title("S.I.M.A")
    janela.configure(bg="black")

    # Criando e posicionando o botão (além de definir o comando que ele executará)
    botao = Button(janela, text="Iniciar", font=("Arialle, 20"), command=chamarbotao)
    botao.grid(column=0, row=0, padx=0, pady=10)

    # Posicionando imagem na tela
    label_image = Label(janela, image=img, border="0")
    label_image.grid(padx=30, pady=0)

    # Iniciando a janela e mantendo ela funcionando  
    janela.mainloop()
################################################################

# Inicia a função que cria a interface do programa
Interface()
