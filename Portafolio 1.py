"""
Nombre: divisores
Entradas: número entero positivo mayor a 0
Salidas: divisores de un número de manera descendente
Restricciones: número entero positivo mayor a 0
"""
def divisores(num):
    if isinstance(num,int) and (num>0):
        return divisores_aux(num,num)
    else:
        print("Error: solo se permiten valores enteros positivos")

def divisores_aux(num,divisores):
    if(divisores==0):
        return None
    else:
        if(num%divisores)==0:
            print(divisores)
            return divisores_aux(num,divisores-1)
        else:
            return divisores_aux(num,divisores-1)


#------------------------------------------------------
"""
Nombre: multiplicarRecursivo
Entradas:
        num: número entero positivo
        factor: número entero positivo
Salidas: la multiplicación de num por factor sin utilizar
         el operador de multiplicación
Restricciones: números enteros positivos
"""
def multiplicarRecursivo(num, factor):
    if isinstance(num,int) and isinstance(factor,int):
        return multiplicar_aux(num, factor)
    else:
        print("El valor debe ser entero positivo")

def multiplicar_aux(num, factor):
    if(factor==0):
        return 0
    else:
        return num+multiplicar_aux(num, factor-1)

#-----------------------------------------------------
"""
Nombre: divisionRecursivo
Entradas:
        divisor: número entero positivo mayor a cero
        dividendo: número entero positivo
Salidas: la división de dividendo por divisor sin utilizar
         el operador de división
Restricciones: números enteros positivos, el divisor
               debe ser mayor a cero
"""

def divisionRecursivo(divisor, dividendo):
    if isinstance(divisor,int) and isinstance(dividendo,int) and divisor>0:
        return divisor_aux(divisor, dividendo)
    else:
        print("El valor debe ser entero positivo y el divisor debe ser mayor a 0")
        

def divisor_aux(divisor, dividendo):
    if(dividendo==0):
        return 0
    elif(dividendo==1):
        return 0
    else:
        return 1+divisor_aux(divisor, dividendo-divisor)

#---------------------------------------------------------------
"""
Nombre: corrimientroAEntero
Entradas: números con decimales
Salidas: pasar los números de la parte decimal a la parte entera
Restricciones: números con decimales
"""

def corrimientoAEntero(num):
    if isinstance(num,float):
        num=num%10**10*10000000
        num=int(num)
        return A_Entero(num,0)
    else:
        print("El valor debe ser un número con decimales")

def A_Entero(num,indice):
    if(num%10)==0 and (num!=0):
        return A_Entero(num//10,indice)
    elif(num==0):
        return 0
    else:
        return num%10*10**indice+A_Entero(num//10,indice+1)
#----------------------------------------------------------------
"""
Nombre: contarDigitosFlotante
Entradas: números con decimales 
Salidas: la cantidad de digitos tomando en cuenta los
         decimales, positivos y negativos
Restricciones: números con decimales
"""

def contarDigitosFlotante(num):
    if isinstance(num,float)and num>0:
        num=num%10**10*10000000
        num=int(num)
        return contarDigitosFlotante(num)
    elif(num==0):
        return 0
    elif(num<0):
        return contarDigitosFlotante(num*-1)
    elif(num%10)==0:
        return contarDigitosFlotante(num//10)
    elif(num>0):
        return 1+contarDigitosFlotante(num//10)
    
    else:
        print("Error: el parametro num no es valido")

#---------------------------------------------------------------
"""
Nombre: indiceNumero
Entradas:
        num: número entero positivo
        indice: número entero positivo mayor o igual a cero
Salidas: devuelve el digito de un número según su indice
Restricciones: números enteros positivos
"""

def indiceNumero(num,indice):
    if isinstance(num,int) and num>0 and isinstance(indice,int):
        if(indice>=0):
           largo=digitos_aux(num)
           funcion=num-1
           return indice_v2(num,indice+1,largo,funcion)
        else:
            print("Error: indice debe ser mayor o igual a cero")
    else:
        print("Error: el parametro no es valido, digite un numero entero positivo")


def digitos_aux(num):
    if(num==0):
        return 0
    else:
        return 1+digitos_aux(num//10)

def indice_v2(num,indice,largo,funcion):
    if(num==0):
        return 0
    elif(num<funcion):
        suma=num%10
        return suma+indice_v2(num%10//10,indice,largo,funcion)
    elif(indice==largo):
        return num%10+indice_v2(num%10//10,indice,largo,funcion)
    else:
        largo=largo-indice
        return indice_v2(num//10**largo,indice,largo,funcion)
    
#----------------------------------------------------------------
"""
Nombre: cortarNumero
Entradas:
        num: número entero positivo
        indice1: número entero positivo
        indice2: número entero positivo
Salidas: devuelve un nuevo número según indices
Restricciones: Números enteros positivos
"""

def cortarNumero(num,indice1,indice2):
    if (isinstance(num,int)
    and num>0
    and isinstance(indice1,int)
    and isinstance(indice2,int)):
        if(indice1>=0) and (indice2>=0):
            numero1=indiceNumero(num,indice1)
            numero2=indiceNumero(num,indice2)
            return contar_aux(numero1,numero2)
        else:
            print("Error: los indices deben ser mayores o iguales a cero")
    else:
        print("Error: el parametro no es valido, digite un numero entero positivo")
        

def contar_aux(numero1,numero2):
    if(numero1==0):
        return 0
    else:
        return numero1*10+numero2+contar_aux(numero1//10,numero2)
        
        
    
