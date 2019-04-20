import math as m
from constant import *


SI = {
    g:K,
    m:'',
    s:'',
    A:'',
    K:'',
    mol:'',
    C:''
}

def join(*values, spliter=''):
    strValues = []
    for value in values:
        if type(value)==type([]) or type(value)==type(()):
            for v in value:
                strValues.append(str(v))
        else:
            strValues.append(str(value))

    return spliter.join(strValues)

class Measure():
    def __init__(self, value, unit, magnitude=''):
        self.value = value*tabConv[magnitude]
        self.unit = unit
        self.measure  = (self.value,unit)
        self.convMeasure = ''.join([str(self.value*tabConv[magnitude]),magnitude,unit])

    def set_convMeasure(self, newMagnitude=''):
        self.convMeasure = ''.join([str(self.value/tabConv[newMagnitude]),newMagnitude,self.unit])
        return self.value/tabConv[newMagnitude]

    def strMeasure(self,newMagnitude=''):
        return ''.join([str(self.value/tabConv[newMagnitude]),newMagnitude,self.unit])
    
    def toSI(self):
        return (self.value/tabConv[SI[self.unit]],SI[self.unit],self.unit)

    
    def strSI(self):
        toSI = self.toSI()
        return ''.join([str(toSI[0]),toSI[1],toSI[2]])

class Metre(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'m',magnitude)


class Gram(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'g',magnitude)

class Ampere(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'A',magnitude)
        self.unitValue =value*Coulomb().unitValue/Second().value,Coulomb().unit
        self.strUnitValue = join(self.unitValue)

class Second(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'s',magnitude)

class Newton(Measure):
    def __init__(self, value=1, magnitude='',Kg=1, m=1, s=1):
        super().__init__(value,'N',magnitude)
        self.unitValue = value*(Gram(Kg,K).set_convMeasure(K)*Metre(m).value/(Second(s).value*Second(s).value))


class Coulomb(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'C',magnitude)
        self.unitValue = elementCharge*value


class Electronvolt(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'s',magnitude)


bloco = Newton(10)

print(bloco.unitValue)








print(Ampere(5).strUnitValue)

