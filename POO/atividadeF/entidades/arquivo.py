from time import ctime
from utils.cor import Cor

class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.tcor = Cor()
        self.conteudo = ['', '', '', '']
        self.data_criacao = ctime()
        self.ultima_modificacao = None
        self.max_chars = 50
        self.tamanho = 0

    def atualizar_data_mod(self):
        self.ultima_modificacao = ctime()

    def get_nome(self):
        return self.nome

    def get_data_criacao(self):
        return self.data_criacao

    def get_data_ultima_modificacao(self):
        return self.ultima_modificacao

    def get_tamanho(self):
        return str(self.tamanho)

    def atualizar_tamanho(self, num_linha, novo):
        self.tamanho -= len(self.conteudo[num_linha]) * 8
        self.tamanho += len(novo) * 8

    def set_linha(self, num_linha, conteudo):
        self.atualizar_tamanho(num_linha, conteudo)        
        self.conteudo[num_linha] = conteudo

    def get_ultima_mod_safe(self):        
        if self.ultima_modificacao:
            return 'Ultima Modificação: ' + self.ultima_modificacao
        else:
            return ''

    def mostrar_conteudo(self):
        print("ARQUIVO:", self.get_nome() + '.txt' + '\t\t' + self.get_ultima_mod_safe())
        print()
        for i in range(4):
            linha = self.get_linha(i)
            self.tcor.print_colorido(str(i + 1) + ' ', 'azul', '')
            print(linha)

    def get_linha(self, num):
        if 0 <= num <= 3:
            return self.conteudo[num]
        else:
            raise Exception("Numero de linha fora do intervalo.")

    def escrever_linha(self, linha, conteudo):
        if len(conteudo) > self.max_chars:
            self.set_linha(linha - 1, conteudo[:self.max_chars])
        else:
            self.set_linha(linha - 1, conteudo)

    def __str__(self):
        return self.get_nome()