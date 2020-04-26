from Models.Estudante import Estudante;
from os import system;

def Cadastro(estudantes):
    nome = ""
    mat = ""
    curso = ""
    placa = ""
    acesso = ""
    
    system('clear')
    
    nome = input("Digite seu nome : ")
    mat = input("Digite sua matrícula : ")
    curso = input("Digite seu curso : ")
    placa = input("Digite a placa do carro : ")
    
    acesso = input("Você possui o cartão DeFis? Sim ou Não? Resposta : ")
    if(acesso == "S" or acesso == "Sim"):
        acesso.replace(acesso,"Sim");

    estudante = Estudante(None,None,None,False,None,None);
    
    if(acesso.upper() == "SIM"):
        estudante.setAcesso(True);
    estudante.setNome(nome)
    estudante.setMatricula(mat)
    estudante.setCurso(curso)
    estudante.setPlaca(placa)
    estudante.setProprietario(estudante.getNome())

    estudantes.append(estudante)

    system('clear')
    print("Cadastro concluído com sucesso!\n")