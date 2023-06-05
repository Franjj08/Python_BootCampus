anio = int(input("Ingres un anio"))
def verificarSiEsbisiest(anio):
    if anio % 4 ==0:
        return True

if verificarSiEsbisiest(anio):
    print("Si es un anio biseisto")
else:
    print("No lo es")