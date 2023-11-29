class Personaje:#Creamos una clase llamada Personaje

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):#metodo (es una funcion)de la clase Metodo constructor. No hace falta declarar por que desde acá ingresaremos al instanciar los valores por defecto de los atributos
        self.nombre = nombre#cambiar el valor del atributo nombre por el que recibas
        self.fuerza = fuerza#cambiar el valor del atributo fuerza por el que recibas
        self.inteligencia = inteligencia#cambiar el valor del atributo inteligencia por el que recibas
        self.defensa = defensa#cambiar el valor del atributo defensa por el que recibas
        self.vida = vida#cambiar el valor del atributo vida por el que recibas


    def atributos(self):#metodo que muestra el ESTADO del objeto o sea el valor de sus atributos ¿set?
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida", self.vida)
    
    
    def subir_nivel(self, fuerza, inteligencia, defensa):#metodo que incrementa la fuerza, inteligencia y defenza ¿get?
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):#metodo para ver si esta vivo ¿get?
        return self.vida > 0#si se cumple retorna True sino False
    
    def morir(self):#metodo para la acción de morir que pone la vida a 0 ¿set?
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    
    def daño(self, enemigo):#metoda para determinar el daño que infligimos a nuestro enemigo
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a ",enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, "es",enemigo.vida)
        else:
            enemigo.morir()

mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)#Aqui asignamos a la variable mi_personaje la clase contructor del obejeto

# mi_personaje.atributos()
# mi_personaje.subir_nivel(1, 2, 0)
# mi_personaje.atributos()

# mi_personaje.morir()
# mi_personaje.atributos()

# mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 100)
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 5)#Si la vida es 5 ante un ataque de 7 esta muerto
# print(mi_personaje.daño(mi_enemigo))
# print(mi_enemigo.vida)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
