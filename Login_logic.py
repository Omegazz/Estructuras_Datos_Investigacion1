"""
Universidad Cenfotec
Estructuras de Datos 2
Investifación 1: Algoritmos de Encriptación Web
Profesor: Christian Sibaja
Estudiantes:
-Marypaz Araya
-Roberto Fernandez
-Diego Salas
Año: 2020
"""
import bcrypt

diccionario = dict()


def create(username, password):
    """Main method to login using bcrypt"""
    # Salt permite tener varios passwords iguales pero se hashean de manera diferente
    # El Salt es por usuario. Cada vez que se genere un password
    # Podemos imprimir bcrypt.gensalt(7)
    if username in diccionario:
        return False
    # Guardamos lo que genere el salt bcrypt.gensalt(7)
    # Cantidad de rehasheos en 7
    diccionario[username] = bcrypt.hashpw(str.encode(password), bcrypt.gensalt(7)).decode("utf-8")
    return True


def login(username, password):
    if not (username in diccionario):
        return False
    # Utiliza el password en bites y el password hasheado para verificar si existe
    # Retorna un booleano
    return bcrypt.checkpw(str.encode(password), diccionario[username].encode("utf-8"))

