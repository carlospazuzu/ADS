from conta import Conta
from time import ctime, time
import hashlib
import sqlite3

class Banco:
    
    def __init__(self, cursor):
        self.cursor = cursor

    def buscar_conta(self, cpf):
        data = self.cursor.execute("SELECT * FROM CONTA WHERE cpf = '{}'".format(cpf)).fetchall()
        if len(data) == 1:
            return Conta(data[0][0], data[0][1], data[0][2], data[0][3])
        else:
            return False

    def criar_conta(self, titular, cpf, senha, valor_inicial = 0):
        c = Conta(titular, cpf, senha, valor_inicial)

        try:
            self.cursor.execute("INSERT INTO conta VALUES ('{}', '{}', '{}', {})".format(titular, cpf, c.get_senha_hash(), valor_inicial))
            hist = "A conta foi criada."
            self.cursor.execute("INSERT INTO historico(cpf, data, desc) VALUES ('{}', '{}', '{}')".format(cpf, ctime(time()), hist))
        except Exception as e:
            print("OCORREU UM ERRO!")
            print(e)

    def acessar_conta(self, cpf, senha):
        c = self.buscar_conta(cpf)

        if not c:
            print("A conta nao existe!")
            return False
        else:           
            
            if c.senha_correta(senha):
                return c
            else:
                print("Senha incorreta!")
                return False

    def salvar_movimentacoes(self, conta):
        self.cursor.execute("UPDATE conta SET saldo = {} WHERE cpf = '{}'".format(conta.get_saldo(), conta.get_cpf()))
        for hist in conta.get_historico():
            self.cursor.execute("INSERT INTO historico(cpf, data, desc) VALUES ('{}', '{}', '{}')".format(conta.get_cpf(), ctime(time()), hist))


    def transferir(self, cpf_de, cpf_para, valor):
        c1 = self.buscar_conta(cpf_de)
        c2 = self.buscar_conta(cpf_para)
        if not c1:
            print("A conta de CPF {} nao existe!".format(cpf_de))
            return

        if not c2:
            print("A conta de CPF {} nao existe!".format(cpf_para))
            return

        if c1.tem_saldo_suficiente(valor):
            c1.set_saldo(c1.get_saldo() - valor)
            c2.set_saldo(c2.get_saldo() + valor)

            hist_de = 'Foi transferido para a conta de CPF {} o valor R$ {}.'.format(cpf_para, valor)
            hist_para = 'Foi creditado o valor R$ {} apos transferencia da conta de CPF {}.'.format(valor, cpf_de)

            # salvar alterações no banco
            self.cursor.execute("UPDATE conta SET saldo = {} WHERE cpf = '{}'".format(c1.get_saldo(), cpf_de))
            self.cursor.execute("UPDATE conta SET saldo = {} WHERE cpf = '{}'".format(c2.get_saldo(), cpf_para))

            self.cursor.execute("INSERT INTO historico(cpf, data, desc) VALUES ('{}', '{}', '{}')".format(cpf_de, ctime(time()), hist_de))
            self.cursor.execute("INSERT INTO historico(cpf, data, desc) VALUES ('{}', '{}', '{}')".format(cpf_para, ctime(time()), hist_para))
            return True
        else:
            print("A conta de CPF {} nao tem saldo o suficiente para a transferencia!".format(cpf_de))
            return False

