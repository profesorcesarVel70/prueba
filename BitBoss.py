class Personaje:#Creamos una clase llamada Personaje
    # #No hace falta declarar atributos con el mentodo con self
    nombre = "Default"#Atributo del objeto Personaje
    fuerza = 0#Atributo del objeto Personaje
    inteligencia = 0#Atributo del objeto Personaje
    defensa = 0#Atributo del objeto Personaje
    vida = 0#Atributo del objeto Personaje

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):#metodo (es una funcion)de la clase 
        self.nombre = nombre#cambiar el valor del atributo nombre por el que recibas
        self.fuerza = fuerza#cambiar el valor del atributo fuerza por el que recibas
        self.inteligencia = inteligencia#cambiar el valor del atributo inteligencia por el que recibas
        self.defensa = defensa#cambiar el valor del atributo defensa por el que recibas
        self.vida = vida#cambiar el valor del atributo vida por el que recibas
        #en el encabezado solo hace falta declarar otros atributos vayan a ser cargados al ser incializados
        # self.aguante = fuerza * vida #atributo derivado surge de valores de otros atributos
        # self.turno = False#variable cuyo valor no depende de argumento
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)#Aqui asignamos a la variable mi_personaje la clase contructor del obejeto
print("El nombre del jugador es", mi_personaje.nombre)#imprimimos el valor del atributo nombre
print("La fuerza del jugador es", mi_personaje.fuerza)#imprimimos el valor del atributo fuerza


  

