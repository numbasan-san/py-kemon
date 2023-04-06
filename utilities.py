
class utilities:

    @staticmethod
    def opciones(texto, opciones):
        valor = "".upper()
        while not valor in opciones:
            valor = input(f'{texto} (Por favor, seleccione una de las opciones dadas). ').upper()
        return valor
    
    @staticmethod
    def pregunta(texto, max):
        valor = ''
        opt = []

        for i in range(max):
            opt.append(str(i + 1))
        while not(valor in opt):
            valor = input(f'{texto} (Por favor, seleccione una de las opciones dadas). ')
        return int(valor)
