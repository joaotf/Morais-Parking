import time;
from os import system;

# Modelos
from Models.Estudante import Estudante;
#

# Funções
from Functions.Entrada import Entrada;
from Functions.Cadastro import Cadastro;
from Functions.Show import Show;
from Functions.Area_Especial import Área_Especial;
#

estudantes = []
estacionamento = ["Vaga Disponível"] * 10;

if __name__ == "__main__":
    menu = 0;
    while(menu != 10):
        menu = input("Menu\n1)Identificação do Veículo\n2)Cadastro de Veículo\n3)Cadastro de Área Especial\n4)Consultar Ocupação do Estacionamento\n5)Cadastrar Eventos\n6)Sair\nOpção : ")
        if(menu == '1'):
            Entrada(estacionamento,estudantes)

        if(menu == '2'):
            Cadastro(estudantes)
        
        if(menu == '3'):
            Área_Especial(estacionamento)

        if(menu == '4'):
            Show(estacionamento)
        
        if(menu == '6'):
            system('clear')
            print("Saindo...")
            time.sleep(0.4)
            break;
            
        if(menu == '7'):
            for y in range(len(estudantes)):
                print(estudantes[y].getNome())
            
