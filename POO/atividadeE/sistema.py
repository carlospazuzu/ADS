from banco import Banco
from conta import Conta
import sqlite3

class Sistema:

    def __init__(self, connection, cursor):
        self.connection = connection
        self.banco = Banco(cursor)  

    def salvar(self)      :
        self.connection.commit()

    def limpar_tela(self):
        for i in range(20):
            print('\n')

    def criar_conta(self):
        titular = input("Digite o nome do Titular: ")
        cpf = input("Digite o CPF do Titular: ")
        senha = input("Digite a senha: ")
        valor = 0

        while True:
            print("Deseja fazer um deposito inicial? S/N ") 
            op = input()
            if op != 'S' and op != 'N':
                print("Por favor, digite S para 'Sim' e N para 'Nao'")
                continue
            else:
                break

        if op == 'S':
            valor = int(input("Digite o valor inicial: "))

        self.banco.criar_conta(titular, cpf, senha, valor)

    def deposito(self):
        cpf = input("Digite o CPF vinculado a conta: ")

        conta = self.banco.buscar_conta(cpf)

        if conta:
            print("TITULAR: {}".format(conta.get_titular()))
            print("CPF: {}".format(conta.get_cpf()))
            valor = int(input("Digite o valor a ser depositado: "))
            conta.deposito(valor)
            self.banco.salvar_movimentacoes(conta)
            print("Deposito realizado com sucesso!")
        else:
            print("\nConta nao encontrada!\n")

    def acessar_conta(self):
        cpf = input("Digite o CPF do titular: ")
        senha = input("Digite a senha: ")
        
        conta = self.banco.acessar_conta(cpf, senha)

        if conta:
            while True:           
                self.salvar()
                self.limpar_tela()     
                print("Titular: {}".format(conta.get_titular()))
                print("Saldo Atual: {}\n".format(conta.get_saldo()))
                
                print("=" * 10 + " *** " + "=" * 10)
                print("1. REALIZAR SAQUE")
                print("2. REALIZAR DEPOSITO")
                print("3. TRANSFERENCIA DE VALORES")
                print("0. SAIR")
                print("=" * 10 + " *** " + "=" * 10)

                op = int(input("\nDigite a opcao: "))

                if op == 1:
                    valor = int(input("Digite o valor de saque: "))
                    if conta.saque(valor):
                        print("Foi sacado R$ {}.".format(valor))                    
                elif op == 2:
                    valor = int(input("Digite o valor para deposito: "))
                    conta.deposito(valor)
                    print("{} reais foram depositados na conta.".format(valor))                        
                elif op == 3:
                    cpf_para = input("Digite o CPF do titular da conta a fazer transferencia: ")
                    valor = int(input("Digite o valor a ser transferido: "))
                    if self.banco.transferir(conta.get_cpf(), cpf_para, valor):
                        conta.set_saldo(conta.get_saldo() - valor)
                        print("Transferencia realizada com sucesso!")
                    else:
                        print("Ocorreu um erro!")
                elif op == 0:
                    self.banco.salvar_movimentacoes(conta)
                    break                

                input("Digite algo para continuar...")
        else:
            print("\nConta nao encontrada\n")

    def run(self):
        while True:
            print("=" * 10 + " *** " + "=" * 10)
            
            print("1. CRIAR NOVA CONTA")
            print("2. REALIZAR DEPOSITO")
            print("3. ACESSAR CONTA")
            print("0. SAIR")
            
            print("=" * 10 + " *** " + "=" * 10)

            print("\n\nDigite a opção desejada: ")
            op = int(input())

            self.limpar_tela()

            if op == 1:
                self.criar_conta()
            elif op == 2:
                self.deposito()
            elif op == 3:
                self.acessar_conta()
            elif op == 0:
                self.banco.cursor.close()
                break


def main():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS conta(titular varchar(50), cpf varchar(20) NOT NULL, senha varchar(50), saldo real, primary key (cpf))")
    cursor.execute("CREATE TABLE IF NOT EXISTS historico(id integer primary key AUTOINCREMENT, cpf varchar(20), data varchar(40), desc varchar(100))")
    sistema = Sistema(conn, cursor)
    sistema.run()
    sistema.salvar()
    conn.close()

if __name__ == '__main__':
    main()