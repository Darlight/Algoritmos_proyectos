"""
Universidad del Valle de Guatemala
CC3041 - Analisis y diseño de algoritmos
Ing. Tomas Galvez
Mario Perdomo
Carnet 18029
proyecto_lamda.py 
"""
#Usando la manera pythonica de los lambdas: https://realpython.com/python-lambda/ 
f = lambda x: x+1
g = lambda x: 2 * x
h = lambda x, y: x**2 + y**2
cero = lambda fn, x:  fn + x
uno = lamnda x: x


  
print("f(5) = " + str(f(5)))
print("g(3) = " + str(g(3)))
print("g(4,4) = " + str(h(4,4)))
print("cero() = " + str(cero(0,0)))
print("uno() =")
print("dos() =")
print("tres() =")
print("sucesor() =")
print("suma() = ")
print("multi() = ")

#print("g({}) = {}".format(2, g(2)))
#print("h({}, {}) = {}".format(3, 4, h(3, 4)))
