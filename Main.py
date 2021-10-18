from Videojuego import Videojuego
from Serie import Serie


Series = list()
Videojuegos = list()


Series.insert(1,Serie(titulo="Mandalorian ", numeroTemp=1, entregado=True))
Series.insert(2,Serie(titulo="The witcher ", numeroTemp=2, entregado=False))
Series.insert(3,Serie(titulo="Breaking Bad ", numeroTemp=3, entregado=True))
Series.insert(4,Serie(titulo="Game of Thrones ", numeroTemp=5, entregado=False))
Series.insert(5,Serie(titulo="The Boys ", numeroTemp=4, entregado=True))

Videojuegos.insert(1,Videojuego(titulo="World of Warcraft ", horasEstimadas=10, entregado=False))
Videojuegos.insert(2,Videojuego(titulo="Fornite ", horasEstimadas=20, entregado=True))
Videojuegos.insert(3,Videojuego(titulo="Leage of legend ", horasEstimadas=30, entregado=False))
Videojuegos.insert(4,Videojuego(titulo="Call of Duty ", horasEstimadas=40, entregado=True))
Videojuegos.insert(5,Videojuego(titulo="Valorant ", horasEstimadas=50, entregado=True))


serieMasTemporadas = Serie()
juegoMasHoras = Videojuego()

def entregar():
    for i in Series:
        if i.entregado:
         print(i)
        if i.numeroTemp > serieMasTemporadas.numeroTemp:
             serieMasTemporadas = i

for i in Videojuegos:
    if i.entregado:
        print(i)
        if i.horasEstimadas > juegoMasHoras.horasEstimadas:
            juegoMasHoras = i

print("\nSerie con mas Temporadas: " + str(serieMasTemporadas))
print("Juego con mas horas estimadas: " + str(juegoMasHoras))