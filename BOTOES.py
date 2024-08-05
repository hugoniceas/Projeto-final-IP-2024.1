class Botao():
    def __init__(self, image, pos, text_input, font, base_color ):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, tela):
        if self.image is not None:
            tela.blit(self.image, self.rect)
        tela.blit(self.text, self.text_rect)

    def mudarCorBase(self, cor):
        self.text = self.font.render(self.text_input, True, cor)