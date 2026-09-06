#single member 
from calculator import add 
from biology import genes 
from physics import newtonsfirst

# #module is not imported 
# print(calculator.add(20,10))
# print(biology.genes())
# print(physics.newtonsfirst())

#written memebers are imported
print(add(20,10))
print(genes())
print(newtonsfirst())

# #other members are not imported
# print(sub(20,10))
# print(newtonssecond())
# print(dna())