from sistema import Sistema

class Aplicacao:

    def __init__(self):
        self.sistema = Sistema()

    def run(self):
        self.sistema.run()

if __name__ == "__main__":
    app = Aplicacao()
    app.run()