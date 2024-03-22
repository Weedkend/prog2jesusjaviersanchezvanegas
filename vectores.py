Nada = []
Colores = ["amarillo", "rojo", "verde", "violeta","naranja"]
print ('colores:', Colores) 
print('colores', len(Colores))
UNO_COLOR = Colores[0]
print("Primer color: ", UNO_COLOR)
DOS_COLOR = Colores[2]
print("Color del medio: ", DOS_COLOR)
TRES_COLOR = Colores[4]
print("Ultimo color: ", TRES_COLOR)

Datos_personales = ['nombre', 'edad', 'altura', 'estado civil', 'dirección']
Datos_personales.append('cedula')
Datos_personales.append('sexo')

it_companies = [ 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(3, 'Falabella')
it_companies.sort()
print("Empresas: ", it_companies)
existe = 'Falabella' in it_companies
print("¿Se encuentra Falabella?", "\n R/=" ,existe)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.pop()
print(it_companies)
del it_companies[0]
print(it_companies)
it_companies.clear()
print(it_companies)