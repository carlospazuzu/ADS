from utils.cor import Cor
from utils.limpar import *

from entidades.disco import Disco
from entidades.editor import Editor
from entidades.stagingarea import StagingArea
from entidades.repositorio import Repositorio

class Sistema:

    def __init__(self):
        self.tcor = Cor()
        self.warning = False
        self.comando = False
        self.cmd = ''

        self.disco = Disco()     
        self.staging = StagingArea()   
        self.repo = Repositorio()

        # aux
        self.tracked = []
        self.untracked = []

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
                elif self.cmd == 'help':
                    print('-' * 20)
                    print('Comandos válidos:')
                    print('-' * 20)
                    print('ls\t\t lista arquivos do diretorio raiz')
                    print('edit <arquivo>\t\t abre o editor de texto')
                    print('touch <arquivo>\t\t criar um novo arquivo de texto')
                    print('rm <arquivo> \t\t deleta arquivo')
                    print('exit\t\t fechar o programa')
                    print('-' * 20)
                    print('Comandos de git:')
                    print('-' * 20)
                    print('git add <arquivo>\t\t adiciona arquivo à staging zone')
                    print('git rm <arquivo> \t\t remove arquivo da staging zone')
                    print('git commit\t\t comita arquivos da SZ ao repositorio')
                    print('git status\t\t mostra o status da staging zone')
                    print('git log\t\t mostra todos os commits realizados')
                    print()
                    input("Digite algo para continuar...")

                elif self.cmd == 'status':     
                    # mostrar apenas se tiver pelo menos 1 arquivo nao rastreado               
                    if len(self.untracked) > 0:
                        print('NAO RASTREADOS:')
                        for arq in self.untracked:                        
                            self.tcor.print_colorido('\t\t' + str(arq) + '.txt', 'vermelho')  
                        print()                                     
                    # mostrar apenas se tiver pelo menos 1 arquivo na staging area
                    if len(self.tracked) > 0:
                        print('STAGING AREA:')
                        for arq in self.tracked:                        
                            self.tcor.print_colorido('\t\t' + str(arq) + '.txt', 'verde')
                        print()                    

                    if len(self.disco) == 0:
                        print("Nao existem arquivos.\n")

                    self.untracked.clear()
                    self.tracked.clear()


            if self.warning:
                self.tcor.print_colorido('Comando inválido\n', 'vermelho')

            print('Para pedir ajuda, digite help\n')
            self.tcor.print_colorido('~/git/', 'azul')        
            print("> ", end='')
            ipt = input()

            self.warning = False
            self.comando = False
            self.cmd = ''

            # fechar aplicação e salvar alterações
            if ipt == 'exit':
                self.repo.encerrar()
                limpar_tela()
                break
            
            # help
            elif ipt == 'help':
                self.comando = True
                self.cmd = 'help'

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
                    # se estiver na staging area, retirar
                    self.staging.rm(arq)                    
                        
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

            # adicionar à staging area -- git add
            elif len(ipt) >= 7 and ipt[:7] == 'git add':
                nome_arquivo = ipt.split()[2]
                arq = self.disco.get_arquivo(nome_arquivo)
                if arq:
                    self.staging.add(arq)
                    print(str(arq) + '.txt foi adicionado à Staging Area')
                else:
                    print("Arquivo não encontrado!")

                input()

            # remover da staging area -- git rm
            elif len(ipt) >= 6 and ipt[:6] == 'git rm':
                nome_arquivo = ipt.split()[2]
                arq = self.disco.get_arquivo(nome_arquivo)
                if arq:
                    self.staging.rm(arq)                    
                else:
                    print("Arquivo não encontrado!")
                    input()
                
            # git status
            elif len(ipt) == 10 and ipt == 'git status':
                # tracked = []
                # untracked = []
                for arq in self.disco.get_arquivos():
                    if str(arq) in self.staging.get_arquivos():
                        self.tracked.append(str(arq))
                    else:
                        self.untracked.append(str(arq))

                self.comando = True
                self.cmd = 'status'

            # git commit 
            elif len(ipt) == 10 and ipt == 'git commit':
                if not self.staging.esta_vazia():
                    qt = len(self.staging.get_arquivos().values())
                    msg = input("Digite a mensagem do commit: ")
                    self.repo.commit(self.staging, msg)
                    print("{} arquivos commitados.".format(qt))
                else:
                    print("Nao existem arquivos na staging area.")
                
                input()

            # git log
            elif len(ipt) == 7 and ipt == 'git log':                
                self.repo.mostrar_commits()
            else:
                self.warning = True