import datetime

hace_cinco_dias = datetime.datetime.now() - datetime.timedelta(days=5)
print(hace_cinco_dias.strftime("%d/%m/%Y"))
print(hace_cinco_dias.weekday())

user_date = datetime.datetime(year=2020, month=1, day=20)
tiempo_restante = user_date - datetime.datetime.now()
print(tiempo_restante)
print(user_date.weekday())

año = int(input("Introduce el año: "))
mes = int(input("Introduce el mes: "))
dia = int(input("Introduce el día: "))

user_date2 = datetime.datetime(year=año, month=mes, day=dia)
tiempo_pasado = datetime.datetime.now() - user_date2
print("Han pasado {} horas.".format(tiempo_pasado.days * 24))