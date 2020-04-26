import time;
from os import system;
import random;


def Clean(estacionamento):
    for z in range(len(estacionamento)-1):
        estacionamento[z] = "Vaga Disponível";

def Área_Especial(estacionamento):
    menu = 0;
    numero = len(estacionamento)*2;
    numeros = [];
    while(menu != 2):
        menu = input("Menu de Áreas Especiais\n1)Indicar Número de Vagas Especiais\n2)Sair\nOpção : ")
        if(menu == '1'):
            system('clear')
            Clean(estacionamento)
            while(numero >= len(estacionamento)):
                system('clear')
                print("O número de vagas especiais não pode ser\nmaior do que o número de vagas totais!\n\n")
                numero = int(input("Digite o número de vagas especiais : "))

            while(numero != 0):
                rand = random.randint(0,len(estacionamento)-1);
                if(rand in numeros):
                    rand = random.randint(0,len(estacionamento)-1);
                else:
                    numeros.append(rand)
                    estacionamento[rand] = "Vaga Especial";
                    numero -= 1;
            system('clear')
            print("Vagas Especiais geradas automaticamente!")
            
        if(menu == '2'):
            system('clear')
            print("Saindo para o menu principal...")
            time.sleep(0.2)
            break;