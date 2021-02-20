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
cero = lambda fn, x:  x
uno = lambda fn, x: fn(x)
dos = lambda fn, x: fn(fn(x))
tres = lambda fn, x: fn(fn(fn(x)))
#vistos en clase
#lambda n: lambda f: lambda x : f(n(f)(x))
sucesor = lambda fn, n, x: fn(n(fn,x))
#lambda a: lambda b: lambda fn: lambda x : a(f)(b(f)(x))
#print(suma(uno)(dos)(f)(1))
suma = lambda fn, a, b, x: a(fn,(b(fn,x)))
#lambda a: lambda b: lambda f: lambda x : a((b)(f))(x)  
multi = lambda fn, a, b, x: a((b,fn),x)




  
print("f(5) = " + str(f(5)))
print("g(3) = " + str(g(3)))
print("g(4,4) = " + str(h(4,4)))
print("cero(f,4) = " + str(cero(f,4)))
print("uno(f,4) = " + str(uno(f,4)))
print("dos(g,4) = " + str(dos(g,4)))
print("tres(f,4) = " + str(tres(f,4)))
print("sucesor(f, dos, 5) = " + str (sucesor(f,dos,5)))
print("suma(f, dos, uno, 3) = " + str(suma(f,dos,uno,3)))
#pruba que suma(f,dos,uno,3) == tres(f,3), quitar el comentario de abajo
#print(tres(f,3))
#print("multi(dos,tres,g,5 = " + str(multi(f,dos,uno,3)))

