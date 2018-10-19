from utils.cor import Cor
from utils.limpar import *

from entidades.disco import Disco
from entidades.editor import Editor

class Sistema:

    def __init__(self):
        self.tcor = Cor()
        self.warning = False
        self.comando = False
        self.cmd = ''

        self.disco = Disco()        

        print()
        print(' ' * 38 + '   ==')
        print(' ' * 38 + '<^\\()/^>')        
        print('█▀▀▀ ░▀░ ▀▀█▀▀ ▀▀█ ░▀░ █▀▀▄ █░░█ █▀▀█  \\/  \\/')
        print('█░▀█ ▀█▀ ░░█░░ ▄▀░ ▀█▀ █░░█ █▀▀█ █░░█   /  \\')
        print('▀▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀▀   `\'\'`')
        print(' ' * 28 + 'ᵈᵒ ˢᵃᵗᵃⁿᵃˢ')
        print('\n\nPressione algo para iniciar...')
        input() 

    def run(self):
        while True:
            limpar_tela()

            if self.comando:
                if self.cmd == 'ls':
                    self.disco.listar()

            if self.warning:
                self.tcor.print_colorido('Comando inválido\n', 'vermelho')

            print('Para pedir ajuda, digite help\n')
            self.tcor.print_colorido('~/git/', 'azul')        
            print("> ", end='')
            ipt = input()

            self.warning = False
            self.comando = False
            self.cmd = ''

            if ipt == 'exit':
                limpar_tela()
                break
            # criar arquivo vazio
            elif len(ipt) >= 5 and ipt[:5] == 'touch':
                nome_arquivo = ipt.split()[1]
                if self.disco.criar_arquivo(nome_arquivo):
                    print(nome_arquivo + '.txt' + ' - Arquivo criado com sucesso!')                    
                else:
                    print('O arquivo já existe!')

                input()
            # editar arquivo existente
            elif len(ipt) >= 4 and ipt[:4] == 'edit':
                nome_arquivo = ipt.split()[1]
                arq = self.disco.get_arquivo(nome_arquivo)
                if arq:
                    edt = Editor(arq)
                    edt.run()                    
                else:
                    print('Arquivo não encontrado!')
                    input()
            # deletar arquivo existente
            elif len(ipt) >= 2 and ipt[:2] == 'rm':
                nome_arquivo = ipt.split()[1]
                arq = self.disco.deletar_arquivo(nome_arquivo)
                if arq:
                    print(nome_arquivo + ".txt deletado com sucesso!")                    
                else:
                    print('Arquivo não encontrado!')
                
                input()
            # listar todos os arquivos do diretorio atual
            elif len(ipt) == 2 and ipt == 'ls':
                self.comando = True
                self.cmd = 'ls'                
            else:
                self.warning = True