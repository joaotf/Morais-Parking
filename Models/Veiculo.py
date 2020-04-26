class Veículo:
    def __init__(self,placa,proprietario):
        self.placa = placa;
        self.proprietario = proprietario;

    def setPlaca(self,placa):
        self.placa = placa;
    def getPlaca(self):
        return self.placa;
    
    def setProprietario(self,proprietario):
        self.proprietario = proprietario;
    def getProprietario(self):
        return self.proprietario;