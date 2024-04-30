def suma(a, b):
    s=a+b 
    return s# Return de la suma

def resta(a, b):
    r=a-b
    return r# Return de la resta

def multiplicacion(a, b):
    m=a*b
    return m# Return de la multiplicación

def division(a, b):
    if b != 0:
        di = a/b
        return di # Return de la división
    else:
        return "Error: división por cero"# Return de error
