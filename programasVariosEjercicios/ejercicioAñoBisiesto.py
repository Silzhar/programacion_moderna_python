year = int(input("Ingrese año : "))

def bisiesto(year):
    if year % 400 == 0 or year % 100 == 0 or year % 4 == 0:
        print("Año bisiesto ")
    else:
        print("El año introducido no es bisiesto")
        
bisiesto(year)

        
        
    