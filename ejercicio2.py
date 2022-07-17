import pickle

class Vehiculo:
    tipo = ''
    color = ''

    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def getInfo(self):
        info = f"Vehículo {self.tipo} de color {self.color}"
        return info

# Creamos objeto v1
v1 = Vehiculo('Sedan', 'Verde')

# Creamos o sobreescribimos archivo donde guardamos la información del objeto
f = open('ej2-datos.bin', 'wb')
pickle.dump(v1, f)
f.close

# leemos y cargamos datos des-serializados
f = open('ej2-datos.bin', 'rb')
v0 = pickle.load(f)
f.close()

print(type(v0))
print(v0.getInfo())
