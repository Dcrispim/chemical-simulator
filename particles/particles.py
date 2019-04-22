import  particles.ElementaryParticles.quark as Quark
import measure.measure as Mens
class Particles():
    def __init__(self,name, m, qUp, qDouwn):
        self.name = name
        self.mass = m.toSI()
        self.qUp = qUp
        self.qDown = qDouwn
Proton = Particles('proton',Mens.Gram(1.6726219,'y'),2,1)
Electron = Particles('electron',Mens.Gram(9.10938356*Mens.p10(-4),'y'),0,0)
Neutron = Particles('neutron',Mens.Gram(1.675,'y'),1,2)