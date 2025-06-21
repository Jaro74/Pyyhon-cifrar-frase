"""texto: Es el mensaje que queremos cifrar, en este caso "Hola Mundo".
desplazamiento: Es el número de posiciones que vamos a mover cada letra en el alfabeto. Aquí es 3."""
def cifrado_cesar(texto, desplazamiento):
    resultado = '' #cadena vacia
    """ Bucle para Recorrer Cada Letra del Texto"""
    for letra in texto:
        if letra.isalpha(): #Verificación si la Letra es Alfabética
            """letra.isupper(): Comprueba si la letra es mayúscula.
                ord('A') o ord('a'): Convierte la letra 'A' o 'a' en su código ASCII (65 para 'A', 97 para 'a').
                Esto asegura que el desplazamiento funcione correctamente tanto para mayúsculas como minúsculas."""
            base = ord('A') if letra.isupper() else ord('a') #Determinar si es Mayúscula o Minúscula
            """ord(letra): Convierte la letra actual en su valor ASCII.
                ord(letra) - base: Normaliza la letra para que 'A' o 'a' sean 0, 'B' o 'b' sean 1, etc.
                + desplazamiento: Aplica el desplazamiento (en este caso, +3).
                % 26: Asegura que si se pasa del final del alfabeto, vuelva al principio (ya que hay 26 letras).
                + base: Convierte de nuevo al rango ASCII correcto (mayúsculas o minúsculas).
                chr(...): Convierte el valor ASCII de nuevo a una letra."""
            resultado += chr((ord(letra) - base + desplazamiento) % 26 + base)
        else:
            resultado += letra
    return resultado

mensaje = "Hola Mundo"
cifrado = cifrado_cesar(mensaje, 3)
print("Texto cifrado:", cifrado)
