class Cor:

    def __init__(self):
        self.off = '\33[0m'
        self.cores = {}        
        self.cores['azul'] = '\33[34m'
        self.cores['amarelo'] = '\33[33m'
        self.cores['verde'] = '\33[32m'
        self.cores['verde-claro'] = '\33[4m'
        self.cores['vermelho'] = '\33[31m'
        self.cores['cinza'] = '\33[90m'

    def print_colorido(self, string, cor, endl='\n'):
        print(self.cores[cor] + string + self.off, end=endl)
