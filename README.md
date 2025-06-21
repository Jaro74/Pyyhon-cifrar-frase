# Programa para cifrar una clase
Texto: Es el mensaje que queremos cifrar, en este caso "Hola Mundo". desplazamiento: Es el número de posiciones que vamos a mover cada letra en el alfabeto. Aquí es 3

## ¿Qué herramientas utilizamos?

 1.  Bucle para Recorrer Cada Letra del Texto
 2. letra.isupper(): Comprueba si la letra es mayúscula. ord('A') o ord('a'): Convierte la letra 'A' o 'a' en su código ASCII (65 para 'A', 97 para 'a'). Esto asegura que el desplazamiento funcione correctamente tanto para mayúsculas como minúsculas.
 3. ord(letra): Convierte la letra actual en su valor ASCII. ord(letra) - base: Normaliza la letra para que 'A' o 'a' sean 0, 'B' o 'b' sean 1, etc. + desplazamiento: Aplica el desplazamiento (en este caso, +3). % 26: Asegura que si se pasa del final del alfabeto, vuelva al principio (ya que hay 26 letras). + base: Convierte de nuevo al rango ASCII correcto (mayúsculas o minúsculas). chr(...): Convierte el valor ASCII de nuevo a una letra
 
