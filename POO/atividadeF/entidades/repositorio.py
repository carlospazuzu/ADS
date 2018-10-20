import sqlite3, string, random
from datetime import datetime


class Repositorio:

    def __init__(self):
        self.db = sqlite3.connect('banco.db')
        self.cursor = self.db.cursor()
        # habilitar leitura e escrita concorrente
        self.cursor.execute('pragma journal_mode=wal')

        self.cursor.execute("CREATE TABLE IF NOT EXISTS commit_repo (id INTEGER AUTO_INCREMENT, hash varchar(7) UNIQUE, msg varchar(20), data TIMESTAMP, PRIMARY KEY(id, hash))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS arquivo (id INTEGER AUTO_INCREMENT PRIMARY KEY, nome varchar(20), hash_commit varchar(7), l1 varchar(50), l2 varchar(50), l3 varchar(50), l4 varchar(50), FOREIGN KEY (hash_commit) REFERENCES commit_repo(hash))")

    # salva alterações no db e fecha com segurança a conexão
    def encerrar(self):
        self.db.close()

    def gerar_hash(self):
        novo_hash = ''
        for i in range(15):
            if random.randint(1, 10) <= 6:
                novo_hash += random.choice(string.ascii_lowercase)
            else:
                novo_hash += random.choice(string.digits)
        
        return novo_hash

    def enviar_obj_commit(self, ghash, msg):
        self.cursor.execute("INSERT INTO commit_repo (hash, msg, data) VALUES (?, ?, ?)", (ghash, msg, datetime.now(),))

    def enviar_arquivo_commitado(self, ghash, arq):
        nome = arq.get_nome()
        l1, l2, l3, l4 = arq.conteudo[0], arq.conteudo[1], arq.conteudo[2], arq.conteudo[3]
        self.cursor.execute("INSERT INTO arquivo(nome, hash_commit, l1, l2, l3, l4) VALUES (?, ?, ?, ?, ?, ?)", (nome, ghash, l1, l2, l3, l4,))

    def novo_commit_arquivos(self, ghash, staging_area):
        # print(staging_area.get_arquivos())
        for arq in staging_area.get_arquivos().values():
            self.enviar_arquivo_commitado(ghash, arq)

    def commit(self, staging_area, msg):
        ghash = self.gerar_hash()

        self.enviar_obj_commit(ghash, msg)
        self.novo_commit_arquivos(ghash, staging_area)

        self.db.commit()

        staging_area.esvaziar()

    def mostrar_commits(self):
        data = self.cursor.execute("SELECT * FROM commit_repo ORDER BY id DESC").fetchall()
        if len(data) > 0:
            for d in data:
                print('\33[91m' + d[3][:19] + '\33[0m', '\33[33m' + d[1] + '\33[0m', d[2])            
        else:
            print("Nenhum commit foi feito")

        input()
        