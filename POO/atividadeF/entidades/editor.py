from utils.limpar import *
from utils.cor import Cor

class Editor:

    def __init__(self, arquivo):
        self.arquivo_atual = arquivo
        self.tcor = Cor()

        self.max_chars = 50

    def run(self):
        while True:
            limpar_tela()
            self.arquivo_atual.mostrar_conteudo()
            print()

            self.tcor.print_colorido('Comandos: mod #, er #, wrt #, exit - # = numero da linha', 'cinza')
            print('> ', end='')
            
            ipt = input()

            # sai do editor e atualiza a data de modificação
            if ipt == 'exit':
                self.arquivo_atual.atualizar_data_mod()
                break
            # er uma linha
            elif len(ipt) == 4 and ipt[:2] == 'er':
                try:
                    num = int(ipt[-1])
                except:
                    print('Digite um numero entre 1 e 4 inclusive.')
                    continue                
                
                self.arquivo_atual.escrever_linha(num, '')
            # escrever uma nova linha
            elif len(ipt) == 5 and ipt[:3] == 'wrt':
                try:
                    num = int(ipt[-1])
                except:
                    print('Digite um numero entre 1 e 4 inclusive.')
                    continue
                
                new = input()
                self.arquivo_atual.escrever_linha(num, new)
            # modifica uma linha existente
            elif len(ipt) == 5 and ipt[:3] == 'mod':
                try:
                    num = int(ipt[-1])
                except:
                    print('Digite um numero entre 1 e 4 inclusive.')
                    continue
                
                linha_mod = self.arquivo_atual.get_linha(num - 1)
                print(linha_mod, end='')

                new = input()

                linha_mod += new
                self.arquivo_atual.escrever_linha(num, linha_mod)


                

