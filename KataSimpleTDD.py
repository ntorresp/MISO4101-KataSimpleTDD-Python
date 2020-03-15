

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
        elif "," in cadena:
            cadenaSplit = cadena.split(",")
            for i in range(0, len(cadenaSplit)):
                cadenaSplit[i] = int(cadenaSplit[i])
            return min(cadenaSplit)
        else:
            return int(min(cadena))

    def maximo(self,cadena):
        if cadena =="":
            return 0
        elif "," in cadena:
            cadenaSplit = cadena.split(",")
            for i in range(0, len(cadenaSplit)):
                cadenaSplit[i] = int(cadenaSplit[i])
            return max(cadenaSplit)
        else:
            return int(cadena)