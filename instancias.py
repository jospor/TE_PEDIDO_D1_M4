class Te:
    def __init__(self):
        pass

te1 = Te()
te2 = Te()

tipo_te1 = type(te1)
tipo_te2 = type(te2)

print(f"El tipo de datos te1 es {tipo_te1}")
print(f"El tipo de datos te2 es {tipo_te2}")  


if tipo_te1 == tipo_te2:
    print("Los tipos son iguales")
else:
    print("Los tipos son diferentes")



