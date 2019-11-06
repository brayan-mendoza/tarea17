#dado un arreglo no vacío de números enteros, 
# regresar el producto de multiplicar sus 
# elementos indentificar la operación básica
a=[1,2,3,4]
b=[2,1]

def multiplicacion(valores):
     resultado=1
               
     for i in range (len(valores)):
         resultado=valores[i] * resultado 
     print("resultado" + str (resultado) )
     
multiplicacion(a)
multiplicacion(b)
