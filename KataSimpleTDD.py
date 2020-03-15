class KataSimpleTDD:
    def contar(self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            cadenaSplit = cadena.split(",")
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

    def maximo(self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            cadenaSplit = cadena.split(",")
            for i in range(0, len(cadenaSplit)):
                cadenaSplit[i] = int(cadenaSplit[i])
            return max(cadenaSplit)
        else:
            return int(cadena)

    def promedio(self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            cadenaSplit = cadena.split(",")
            sumaParcial = 0
            for valor in cadenaSplit:
                sumaParcial += int(valor)
            cantidadValores = len(cadenaSplit)
            return sumaParcial / float(cantidadValores)
        else:
            return int(cadena)

    def resultado(self, cadena):
        result = [self.contar(cadena), self.minimo(cadena), self.maximo(cadena), self.promedio(cadena)]
        return result
