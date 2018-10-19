from entidades.arquivo import Arquivo

class Disco:

    def __init__(self):
        self.arquivos = []

    def get_arquivo(self, nome):
        for arquivo in self.arquivos:
            # TODO modificar o metodo para aceitar arquivos e diretorios
            if arquivo.get_nome() == nome:
                return arquivo

        return None

    def criar_arquivo(self, nome_arquivo):
        for arq in self.arquivos:
            if arq.get_nome() == nome_arquivo:
                return False

        self.arquivos.append(Arquivo(nome_arquivo))

        return True

    def deletar_arquivo(self, nome_arquivo):
        arq = self.get_arquivo(nome_arquivo)

        if arq:
            self.arquivos.remove(arq)
            return True
        else:
            return False

    def listar(self):
        # TODO modificar pra mostrar o diretorio atual (se for o caso)
        print('ARQUIVOS NO DIRETORIO ATUAL:')
        print()
        for arq in self.arquivos:
            print(arq.get_tamanho() + ' bytes' + '\t\t' + str(arq) + '.txt')

        print()
