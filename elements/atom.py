from elements.constant import *
from particles import particles as Part
import measure.measure as Mens


elemwtons = [
    None,
    '1s1',
    '1s2',
    '1s2 2s1'

]
Level = {
    'K':2,
    'L':8,
    'M':18,
    'N':32,
    'O':32,
    'P':18,
    'Q':2
    }
replaceLv = {
    'K':1,
    'L':2,
    'M':3,
    'N':4,
    'O':5,
    'P':6,
    'Q':7
}
subLevel = {
    's': 2,
    'p':6,
    'd':10,
    'f':14
}


class Atom():
    def __init__(self, name,e, p, n):
        '''
        :param name:[String] Element Name
        :param e: [Int] Number of Electrons
        :param p: [Int] Number of Protons
        :param n: [Int] Number or Neutrons
        '''
        self.name = name
        self.protons = p
        self.neutrons = n
        self.setElectConfig(e)
        self.setValence()
        self.setMass()
    
    # esse trecho distribui os eletrons nos Nives (K,L,M,N,O,P,Q)
    def setElectConfig(self, electrons):
        Ks = ('K', 's')
        Ls = ('L', 's')
        Lp = ('L', 'p')
        Ms = ('M', 's')
        Mp = ('M', 'p')
        Md = ('M', 'd')
        Ns = ('N', 's')
        Nd = ('N', 'd')
        Np = ('N', 'p')
        Nf = ('N', 'f')
        Os = ('O', 's')
        Op = ('O', 'p')
        Od = ('O', 'd')
        Of = ('O', 'f')
        Ps = ('P', 's')
        Pp = ('P', 'p')
        Pd = ('P', 'd')
        Qs = ('Q', 's')
        Qp = ('Q', 'p')

        order = [
            [Ks],
            [Ls],
            [Lp, Ms],
            [Mp, Ns],
            [Md, Np, Os],
            [Nd, Op, Ps],
            [Nf, Od, Pp, Qs],
            [Of, Pd, Qp]
        ]
        # Ks2 Ls2 Lp6 Ms2 Mp6 Ns2 Od6
        LevelConfig = {}
        subLevelConfig = {}

        electRemaining = electrons

        i = 0
        for layer in order:

            for l in layer:
                i += 1
                if electRemaining > 0 and (sum(LevelConfig.values()) - electrons) < 0:
                    level = l[0]
                    sub = l[1]
                    if electRemaining > subLevel[sub]:

                        try:
                            LevelConfig[level] += subLevel[sub]
                        except KeyError:
                            LevelConfig[level] = subLevel[sub]

                        electRemaining = electRemaining - subLevel[sub]

                    else:

                        try:
                            LevelConfig[level] += electRemaining
                        except KeyError:
                            LevelConfig[level] = electRemaining

                        electRemaining = 0
                        break


                else:
                    break

        electRemaining += electrons
        for layer in order:

            for l in layer:

                if electRemaining > 0 and (sum(subLevelConfig.values()) - electrons) < 0:
                    level = l[0]
                    sub = l[1]
                    lvSub = ''.join([str(replaceLv[level]), sub])
                    try:
                        subLevelConfig[lvSub] = subLevelConfig[lvSub]
                    except KeyError:
                        subLevelConfig[lvSub] = 0

                    if electRemaining > subLevel[sub] and subLevelConfig[lvSub] <= subLevel[sub]:
                        subLevelConfig[lvSub] += subLevel[sub]

                        electRemaining = electRemaining - subLevel[sub]

                    elif electRemaining <= subLevel[sub] and subLevelConfig[lvSub] <= subLevel[sub]:
                        subLevelConfig[lvSub] += electRemaining

                        electRemaining = 0
                        break


                else:
                    break


        self.levels = LevelConfig
        self.subLevels = subLevelConfig

    def setValence(self):
        lastLevel = 0
        maxElectronNumber = 0
        keys = self.subLevels.keys()
        for key in keys:
            if int(key[0])>lastLevel:
                lastLevel = int(key[0])

        for key in keys:
            if int(key[0]) == lastLevel and self.subLevels[key] > maxElectronNumber:
                maxElectronNumber = self.subLevels[key]


        self.valence = maxElectronNumber
        self.lastLavel = lastLevel

    def setMass(self):
        massElect = sum(self.subLevels.values())*Part.Electron.mass[0]
        massProton = self.protons*Part.Proton.mass[0]
        massNeutron = self.neutrons*Part.Neutron.mass[0]


        self.mass =(massNeutron+massProton+massElect)/Mens.Dalton().unitValue[0],Mens.Dalton().unit
        self.massG = Mens.toBase(((massNeutron+massProton+massElect),'g','K'))
        #self.mass = P.Electron
    # criação do atomo ATOMO(numero de eletrons, numero de protons, numero de neutrons)

C = Atom('carbon',92,92,145)
print(C.massG)