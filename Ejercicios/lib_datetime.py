import datetime

hace_cinco_dias = datetime.datetime.now() - datetime.timedelta(days=5)
print(hace_cinco_dias.strftime("%d/%m/%Y"))
print(hace_cinco_dias.weekday())

user_date = datetime.datetime(year=2020, month=1, day=20)
tiempo_restante = user_date - datetime.datetime.now()
print(tiempo_restante)
print(user_date.weekday())

born_date = (input("¿Cuál es tu fecha de nacimiento? (dd/mm/yyyy): "))
born_date = datetime.datetime.strptime(born_date, "%d/%m/%Y")

tiempo_pasado = datetime.datetime.now() - born_date
print("Has vivido {} horas o {} días.".format(tiempo_pasado.days * 24, tiempo_pasado.days))
