from os import system;

def Entrada(estacionamento,estudantes):
    acesso = False;
    local = 0;
    vagas = len(estacionamento);
    vaga_not_ocupped = False;
    system("clear")    
    placa = input("Digite a placa do carro : ")
    for x in range(len(estudantes)):
        if(placa == estudantes[x].getPlaca()):
            acesso = True;
            local = x;
    if(acesso == True and vaga_not_ocupped == False):
        system("clear")
        print("Acesso Autorizado!\n\n")
        while(vaga_not_ocupped == False):
            index = int(input(f"Vagas disponíveis: {vagas}\nNúmero da Vaga : "))
            if(estacionamento[index] == 'Vaga Disponível'):
                estacionamento[index] = estudantes[local].getPlaca()
                print(f"Vaga ocupada por {estudantes[local].getNome()}")                 
                vagas -= 1;
                acesso = False;
                vaga_not_ocupped = True;
            else:
                system('clear')
                print("Vaga ocupada!");
                index = int(input(f"Vagas disponíveis: {len(estacionamento)}\nNúmero da Vaga : "))
    else:
        system("clear")
        print("Placa não reconhecida!")
