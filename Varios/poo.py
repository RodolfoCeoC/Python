""" class Humano:
    def __init__(self) -> None:
        print("Soy un humano")
    
    def hablar(self, mensaje):
        print(mensaje)
        
Rodolfo = Humano()

Rodolfo.hablar("Puedo hablar") """


class Tarjeta:
     def __init__(self, numero, cantidad = 0):
         self.numero = numero
         self.saldo = cantidad
         return
     def __str__(self):
         return 'Tarjeta número {} con saldo {:.2f}€'.format(self.numero, self.saldo)
t = Tarjeta('0123456789', 1000)
print(t)