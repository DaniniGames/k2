import datetime
import random

AVERAGE_LIFESPAN = 84
SMOKE_PENALIZATION = 4
DRINKER_PENALIZATION = 4
COKE_PENALIZATION = 6
SEDENTARY_PENALIZATION = 10


def text_with_underscores(x):
    print(x)
    print(len(x) * "_")


def ask_yes_or_not(message):
    response = None
    while response != "s" and response != "n":
        response = input(message + " [s/n]")
    return response == "s"


text_with_underscores("Averigua cuanto te queda de vida")

born_date = (input("¿Cuál es tu fecha de nacimiento? (dd/mm/yyyy): "))
born_date = datetime.datetime.strptime(born_date, "%d/%m/%Y")
years_lost = 0

if ask_yes_or_not("¿Fumas?"):
    years_lost += SMOKE_PENALIZATION

if ask_yes_or_not("¿Bebes?"):
    years_lost += DRINKER_PENALIZATION

if ask_yes_or_not("¿Te gusta la coca?"):
    years_lost += COKE_PENALIZATION

if not ask_yes_or_not("¿Haces deporte?"):
    years_lost += SEDENTARY_PENALIZATION

base_lifespan = random.randint(int(AVERAGE_LIFESPAN / 1.25), AVERAGE_LIFESPAN)
lifespan = base_lifespan - years_lost
death_day = born_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de muerte: {}. Te quedan {} días de vida y caerá en {}.".format(death_day.strftime("%d/%m/%Y"), days_to_death.days, death_day.strftime("%A")))