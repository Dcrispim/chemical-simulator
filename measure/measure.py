import math
from measure.constant import *

def Constant(constantName):
    constants = {
        '0k': Celsius(-273.15).value,
        'g': Acceleration(9.80665),
        'c':Velocity(299792458).value,
        'c2':(pow(Velocity(299792458).value,2),Velocity().unit),
        'L': 6.02214076*p10(23)

    }
    return constants[constantName]

SI = {
    'g':'K',
    'm':'',
    's':'',
    'A':'',
    'K':'',
    'mol':'',
    'C':''
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

def toBase(Measure):
    value = Measure[0]
    unit = Measure[1]
    try:
        magnitude = Measure[2]
    except:
        magnitude = ''
    return value*tabConv[magnitude],unit

def converter(Measure,Scale=''):
    M = toBase(Measure)
    value = M[0]/tabConv[Scale]
    if Scale=='':
        return value, M[1]
    else:
        return value, M[1], Scale


def operate(Measure1,Measure2,operator='*', si=False):
    M1 = toBase(Measure1)
    M2 = toBase(Measure2)
    unit = M1[1]
    if M1[1]==M2[1]:

        if operator=='*':
            result = M1[0]*M2[0]

    if si:
        return converter((result,unit),SI[unit])
    else:
        return result,unit


class Measure():
    def __init__(self, value, unit, magnitude=''):
        self.value = value*tabConv[magnitude]
        self.unit = unit
        self.measure  = (self.value,unit)
        self.convMeasure = ''.join([str(self.value*tabConv[magnitude]),magnitude,unit])

    def __call__(self, value=1, *args, **kwargs):
        return self.value,self.unit


    def set_convMeasure(self, newMagnitude=''):
        self.convMeasure = ''.join([str(self.value/tabConv[newMagnitude]),newMagnitude,self.unit])
        return self.value/tabConv[newMagnitude]

    def strMeasure(self,newMagnitude=''):
        return ''.join([str(self.value/tabConv[newMagnitude]),newMagnitude,self.unit])
    
    def toSI(self):
        return (self.value/tabConv[SI[self.unit]],self.unit,SI[self.unit])

    
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
        self.unitValue = value*(Gram(Kg,'K').set_convMeasure('K')*Metre(m).value/(Second(s).value*Second(s).value)),'Kg*m/s²'
        self.strUnitValue = join(self.unitValue)
class Coulomb(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'C',magnitude)
        self.unitValue = elementCharge*value,self.unit
        self.strUnitValue = join(self.unitValue)
class Electronvolt(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'eV',magnitude)
        self.unitValue =value*Joule(160.217733,'z').value,Joule().unit
        self.strUnitValue = join(self.unitValue)
class Celsius(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'°C',magnitude)
class Joule(Measure):
    def __init__(self, value=1, magnitude='', Kg=1, m=1, s=1):
        super().__init__(value,'J',magnitude)
        self.unitValue = value*(Gram(Kg,'K').set_convMeasure('K'))/(math.pow(Metre(m).value,2)/math.pow(Second(s).value,2)),'Kg*(m²/s²)'
        self.strUnitValue = join(self.unitValue)
class Velocity(Measure):
    def __init__(self, value=1, magnitude='', m=1, s=1):
        super().__init__(value,'m/s',magnitude)
        self.unitValue =Metre(m).value/Second(s).value,self.unit
        self.strUnitValue = join(self.unitValue)
class Acceleration(Measure):
    def __init__(self, value=1, magnitude='', v=1, s=1):
        super().__init__(value,'m/s²',magnitude)
        self.unitValue =Velocity(v).value/Second(s).value,self.unit
        self.strUnitValue = join(self.unitValue)
class Dalton(Measure):
    def __init__(self, value=1, magnitude=''):
        super().__init__(value,'u',magnitude)
        self.unitValue = value*Gram(1.660539040*p10(-27),'K').toSI()
        self.strUnitValue = join(self.unitValue)
