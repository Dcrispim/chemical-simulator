import math

def p10(x):
    return math.pow(10,x)

def p60(x):
    return math.pow(60,x)

y='y'
z='z'
a='a'
f='f'
p='p'
n='n'
u='µ'
m='m'
c='c'
d='d'
H='H'
K='K'
M='M'
G='G'
T='T'
P='P'
E='E'
Z='Z'
Y='Y:'

g='g'
s = 's'
A = 'A'
mol ='mol'
C = 'C'
D='D'
S='S'
Dec = 'Dec'
X='X'

elementCharge = 1.60217687*p10(-19)

tabConv = {
    '':1,
    y:p10(-24),
    z:p10(-21),
    a:p10(-18),
    f:p10(-15),
    p:p10(-12),
    n:p10(-9),
    u:p10(-6),
    m:p10(-3),
    c:p10(-2),
    d:p10(-1),
    H:p10(2),
    K:p10(3),
    M:p10(6),
    G:p10(9),
    T:p10(12),
    P:p10(15),
    E:p10(18),
    Z:p10(21),
    Y:p10(24)
}


tabTime ={
    s:1,
    m: p60(1),
    H: p60(2),
    D:p60(2)*24,
    S:(p60(2)*24)*7,
    M:(p60(2)*24)*30,
    A:(p60(2)*24)*365,
    X:((p60(2)*24)*365)*10,
    C:((p60(2)*24)*365)*100,
    C:((p60(2)*24)*365)*1000,

}


measureName = {'m':'metre',
           'l':'liter',
           'g':'gram',
           's':'second',
           'A':'ampere',
           'mol':'mol'
           }
