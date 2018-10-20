class StagingArea:

    def __init__(self):
        self.arquivos = {}

    def esta_vazia(self):
        return len(self.arquivos) == 0

    def esta_embarcado(self, arquivo):
        return str(arquivo) in self.arquivos            

    def add(self, arquivo):
        self.arquivos[str(arquivo)] = arquivo

    def rm(self, arquivo):
        if self.esta_embarcado(arquivo):
            del self.arquivos[str(arquivo)]

    def get_arquivos(self):        
        return self.arquivos
    
    def esvaziar(self):
        self.arquivos.clear()