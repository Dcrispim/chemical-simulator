import measure.measure as M

class Quark():
    def __init__(self, name, symbol, energy, mass, color, spin ):
        self.name = name
        self.energy = M.Coulomb(energy).measure
        self.mass = M.Electronvolt(mass,'M').unitValue[0]/M.Constant('c2')[0]
        self.color = color
        self.spin = spin
        self.symbol = symbol


Up = Quark('qUp','u',-(1/3),4.8,True,1/2)
Down = Quark('qDown','d',2/3,2.3,True,1/2)