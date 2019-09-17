palabras = dict()
string = "Hola Hola McKim Kim Kim Kim eres un poquito negro negro."
palabras["Hola"] = 1
palabras["McKim"] = 0
palabras["Kim"] = 2
palabras["eres"] = 0
palabras["un"] = 0
palabras["poquito"] = 0
palabras["negro"] = 1

if "Hola" in palabras:
    palabras["Hola"] += 1
if "McKim" in string:
    palabras["McKim"] += 1
if "Kim" in string:
    palabras["Kim"] += 1
if "eres" in string:
    palabras["eres"] += 1
if "un" in string:
    palabras["un"] += 1
if "poquito" in string:
    palabras["poquito"] += 1
if "negro" in string:
    palabras["negro"] += 1

print(palabras)