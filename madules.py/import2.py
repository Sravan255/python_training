#multiple import 
import biology, physics, calculator 

# #members are not imported
# print(dna())
# b = Biology() 
# print(b1)
# print(add(20,10))
# c = Calculator()
# print(c1)
# print(newtonsfirst())
# p = Physics() 
# print(p1)

#modules are imported 
print(biology.dna())
b = biology.Biology() 
print(biology.b1)
print(calculator.add(20,10))
c = calculator.Calculator()
print(calculator.c1)
print(physics.newtonsfirst())
p = physics.Physics() 
print(physics.p1)