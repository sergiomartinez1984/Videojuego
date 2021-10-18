class Videojuego:
    def __init__(self, titulo = " ", horasEstimadas = 10, entregado = False, genero = " ", compañia = " "):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.compañia = compañia

    def __str__(self):
        return str(self.titulo + ", " + repr(self.horasEstimadas) + ", " +  repr(self.entregado) + ", " + self.genero + ", " + self.compañia)


    def get_titulo(self):
        return self.titulo

    def set_titulo(self):
        return self.titulo

    def get_horasEstimadas(self):
        return self.horasEstimadas

    def set_horasEstimadas(self):
        return self.horasEstimadas

    def get_genero(self):
        return self.genero

    def set_genero(self):
        return self.genero

    def get_compañia(self):
        return self.compañia

    def set_compañia(self):
        return self.compañia