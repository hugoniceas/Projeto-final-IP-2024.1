class InfoCarro:
    def __init__(self):
        self.info_carros = [[True, 0, 'assets/sprites/car_red.png'],
                       [False, 50, 'assets/sprites/car_blue.png'],
                       [False, 50, 'assets/sprites/car_yellow.png'],
                       [False, 50, 'assets/sprites/car_white.png'],
                       [False, 0, 'assets/sprites/car_gold.png']]

    def set_comprou(self, idx_carro):
        self.info_carros[idx_carro][0] = True

    def get_comprou(self, idx_carro):
        return self.info_carros[idx_carro][0]

    def get_preco(self, idx_carro):
        return self.info_carros[idx_carro][1]

    def get_path(self, idx_carro):
        return self.info_carros[idx_carro][2]
