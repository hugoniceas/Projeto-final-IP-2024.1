class GameState:
    def __init__(self, nome, run, proximo_estado):
        self.nome = nome
        self.run = run
        self.proximo_estado = ''

    def get_run(self):
        return self.run

    def set_run(self, ligar):
        self.run = ligar

    def set_next_state(self, prox):
            self.proximo_estado = prox

    def get_next_state(self):
            return self.proximo_estado