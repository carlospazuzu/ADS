import hashlib
from time import time, ctime

class Conta:

    def __init__(self, titular, cpf, senha, valor_inicial = 0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = valor_inicial
        self.senha = senha# hashlib.sha1(senha.encode('utf-8')).hexdigest()        
        self.historico = []

    def senha_correta(self, senha):        
        return self.senha == senha

    def get_titular(self):
        return self.titular

    def get_cpf(self):
        return self.cpf

    def get_saldo(self):
        return self.saldo

    def get_senha_hash(self):
        return self.senha

    def get_historico(self):
        return self.historico

    def set_saldo(self, novo_valor):
        self.saldo = novo_valor

    def tem_saldo_suficiente(self, valor):
        return self.saldo >= valor

    def atualizar_historico(self, evento):
        self.historico.append(evento)

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(ctime(time()) + " - Foi depositado R$ {}.".format(valor))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(ctime(time()) + " - Foi sacado R$ {}.".format(valor))
            return True
        else:
            print("A conta nao possui saldo o suficiente!")
            return False

    