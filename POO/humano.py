class Humano():
    
    def __init__(self, cabeza, brazos, piernas):
        self.head = cabeza
        self.arm = brazos
        self.leg = piernas
    
    def __str__(self) -> str:
        human = 'Soy humano y tengo {} cabeza, {} brazos y {} piernas'.format(self.head, self.arm, self.leg)
        return human
    
arg_human = Humano(1, 2, 2)
print(arg_human)