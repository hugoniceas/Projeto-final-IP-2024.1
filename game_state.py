class GameState:
    def __init__(self, nome, run, proximo_estado):
        self.nome = nome
        self.run = run
        self.proximo_estado = proximo_estado

    def get_run(self):
        return self.run

    def set_run(self, ligar):
        self.run = ligar

    def set_next_state(self, prox):
            self.proximo_estado = prox

    def get_next_state(self):
            return self.proximo_estado

    def escrever_texto_opcoes(self, texto, fonte, posicao_x, posicao_y, tela):
        mensagem = fonte.render(texto, True, (255, 255, 255))
        sombra = fonte.render(texto, True, (0, 0, 0))
        tela.blit(sombra, (posicao_x - 5, posicao_y - 2))
        tela.blit(mensagem, (posicao_x, posicao_y))