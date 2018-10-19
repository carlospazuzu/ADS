class Diretorio:

    def __init__(self):
        self.arquivos = []
        self.is_dir = True

    def get_arquivos(self):
        return self.arquivos

    def __len__(self):
        return len(self.arquivos)