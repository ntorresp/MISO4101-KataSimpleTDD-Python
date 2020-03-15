

class KataSimpleTDD:
    def contar(self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            cadenaSplit= cadena.split(",")
            return len(cadenaSplit)
        else:
            return len(cadena)

    def minimo(self, cadena):
        if cadena == "":
            return 0
        else:
            return int(min(cadena))