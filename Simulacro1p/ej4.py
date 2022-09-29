
class PacMan:

    def __init__(self):
        self.puntos = 0
        self.vidas = 3               # Velocidad Puede ser opcional. Puede ser como metodo o atributo.
        
    def velocidad(self):                    #como metodo 
        return 2 + self.puntos / 100

    def comerBolita(self, cantidad):
        self.puntos = self.puntos + (cantidad * 2) 

    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("GAME OVER") 

    def comerFantasma(self, fantasma):
        if fantasma == "Rojo":
            self.puntos += 2
        elif fantasma == "Rosa":
            self.puntos += 8
        elif fantasma == "Naranja":
            self.puntos += 4
        elif fantasma == "Verde":
            self.puntos += 6

pacman = PacMan()

# pacman.comerBolita(22)
# pacman.perderVida()
# pacman.comerFantasma("Rojo")
# pacman.comerFantasma("Rosa")
# print(pacman.puntos)
# pacman.comerBolita(20)
# print(pacman.velocidad())
# pacman.perderVida()
# pacman.perderVida()

# 10
# 2.5
# GAME OVER

# B) Pac-Man nuevas habilidades:

# Ganar una vida extra si llega a 200 puntos, restando esta cantidad de puntos al puntaje
# Además ahora gana más velocidad a medida que suma puntos de la forma: velocidad = 3 + puntos / 100.
 
# Definí la clase PacManMejorado que herede de PacMan, pero que además entienda:
# vidaExtra(): comprobar si se cumple con la condición y aumentar en 1 la cantidad de vida
# y en caso contrario debe aparecer un cartel indicando cuántos puntos le faltan para conseguir una nueva vida.
# 
# También se tiene que redefinir el método velocidad() para que cumpla con lo indicado.

class PacManMejorado(PacMan):

    def vidaExtra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print ("Faltan", 200 - self.puntos, "puntos para ganar una vida extra") 
    
    def velocidad(self):                    #como metodo 
        return 3 + self.puntos / 100

pacmanMejorado = PacManMejorado()

# Ejecutando las siguientes líneas:

pacmanMejorado.comerBolita(22)
pacmanMejorado.perderVida()
pacmanMejorado.comerFantasma("Rojo")
pacmanMejorado.comerFantasma("Rosa")
print(pacmanMejorado.puntos)
pacmanMejorado.comerBolita(80)
print(pacmanMejorado.velocidad())
print(pacmanMejorado.vidas)
pacmanMejorado.comerBolita(30)
pacmanMejorado.vidaExtra()
print(pacmanMejorado.vidas)
pacmanMejorado.vidaExtra()
pacmanMejorado.perderVida()
pacmanMejorado.perderVida()
pacmanMejorado.perderVida()


# El resultado de esto debería ser:	
# 10
# 4.7
# 2
# 3
# Faltan 170 puntos para ganar una vida extra
# GAME OVER