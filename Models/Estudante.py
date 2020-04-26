from Models.Veiculo import Veículo;

class Estudante(Veículo):
    def __init__(self,nome,matricula,curso,acesso,placa,proprietario):
        super().__init__(placa,proprietario)
        self.nome = nome;
        self.matricula = matricula;
        self.curso = curso;
        self.acesso = acesso;
        
    def setNome(self,nome):
        self.nome = nome;
    def getNome(self):
        return self.nome;
        
    def setMatricula(self,matricula):
        self.matricula = matricula;
    def getMatricula(self):
        return self.matricula;

    def setCurso(self,curso):
        self.curso = curso;
    def getCurso(self):
        return self.curso;

    def setAcesso(self,acesso):
        self.acesso = acesso;
    def getAcesso(self):
        return self.acesso;
