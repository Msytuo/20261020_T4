"""
Vamos a hacer un bot, con el que simulemos una conversacion real.

Sera simple, no preguntara cosas complejas, ni devolvera respuestas muy variables.

"""
#Primero le pedimos el nombre
nombre = input("Hey, que tal? Cual es tu nombre? ")
#


CURRENT_YEAR = 2026
CURRENT_MONTH = 10
CURRENT_DAY = 20

#Vamos a pedirle el year de nacimiento
year = int(input(f"Encantado {nombre}, en que ano naciste? "))

#Le pedimos el mes, pero vamos a cerrarle las opciones
meses = { 
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

month = input("En que mes naciste? ")
month_number = meses[month.lower()]

#Pedimos el dia

day = int(input("En que dia naciste? "))

#Primeros vamos a validar que el year y el mes son posibles

while year > CURRENT_YEAR or month not in meses or day > 31:
    
    raise ValueError("No estas diciendo cosas senasatas chaval, te toca reiniciar el programa")
    
# Mostramos todas las variables introducidas
print("Dia", day, "Mes", month, "Ano", year, "Mes en número", month_number)

#Comenzamos el calculo de la edad
edad = CURRENT_YEAR - year

if month_number > CURRENT_MONTH or (month_number == CURRENT_MONTH and day > CURRENT_DAY):
     edad -=1
     print(f"Bueno todavia te queda un poco para sentirte mas mayor este año, tienes {edad} todavia. ")
elif month_number == CURRENT_MONTH and day == CURRENT_DAY:
    print(f"Ey tio muchas felicidades, un año mas viejo eres ya. Cumpliste {edad}. ")

else:
    print(f"Tu ya como si no hubiese tenido un año menos. Tienes {edad} años.")

if edad == 18:
    print(f"Chaval que ya te pueden meter en la carcel. ")
elif edad >= 50:
   padel = input("Un padel el domingo o que? ")

elif 30<= edad < 50:
    print("Pues parece que tienes 20 años cotizados. ")

else:
    print("Disfruta de esta etapa de la vida. ")

