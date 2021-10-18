class Serie:
    def __init__(self, titulo = " ", numeroTemp = 3, entregado = False, genero = " ", creador = " "):
        self.titulo = titulo
        self.numeroTemp = numeroTemp
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    def __str__(self):
        return str(self.titulo + ", " + repr(self.numeroTemp) + ", " + repr(self.entregado) + ", " + self.genero + ", " + self.creador)

    def get_titulo(self):
        return self.titulo

    def set_titulo(self):
        return self.titulo

    def get_numeroTemp(self):
        return self.numeroTemp

    def set_numeroTemp(self):
        return self.numeroTemp

    def get_genero(self):
        return self.genero

    def set_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    def set_creador(self):
        return self.creador