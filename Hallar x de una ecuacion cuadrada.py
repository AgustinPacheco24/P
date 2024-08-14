print("Este programa hallara 'x' de cualquier exprecion")
print("                Ax^2+Bx+C=0                     ")
A=float(input("Ingrese el valor de A = "))
B=float(input("Ingrese el valor de B = "))
C=float(input("Ingrese el valor de C = "))

if B**2 >= 4*A*C:
     X1=(-B+((B**2-4*A*C)**0.5))/2*A
     X2=(-B-((B**2-4*A*C)**0.5))/2*A
     print(f"X1= {X1} , y X2= {X2}")
else:
    print("X no tiene solucion o no existe")