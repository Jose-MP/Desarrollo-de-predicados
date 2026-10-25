# HECHOS 
hechos_animales = {
    "guepardito": {
        "tipo": "individuo",
        "tiene_pelo": True,
        "da_leche": True,
        "come_carne": True,
        "color_leonado": True,
        "manchas_oscuras": True,
        "rayas_negras": False
    },
    "tigrito": {
        "tipo": "individuo",
        "tiene_pelo": True,
        "da_leche": True,
        "come_carne": True,
        "rayas_negras": True,
        "manchas_oscuras": False
    },
    "jirafita": {
        "tipo": "individuo",
        "tiene_pelo": True,
        "da_leche": True,
        "tiene_pezunas": True,
        "cuello_largo": True,
        "manchas_oscuras": True
    },
    "cebrita": {
        "tipo": "individuo",
        "tiene_pelo": True,
        "da_leche": True,
        "tiene_pezunas": True,
        "rayas_negras": True
    },
    "pinguinito": {
        "tipo": "individuo",
        "tiene_plumas": True,
        "nada": True,
        "blanco_y_negro": True
    },
    "albatrocito": {
        "tipo": "individuo",
        "tiene_plumas": True,
        "vuela_bien": True
    },
    "buhito": {
        "tipo": "individuo",
        "tiene_plumas": True,
        "vuela": True,
        "pone_huevos": True,
        "es_nocturno": True,
        "ojos_frontales": True,
        "tiene_penachos": True
    },
    "lechuzita": {
        "tipo": "individuo",
        "tiene_plumas": True,
        "vuela": True,
        "pone_huevos": True,
        "es_nocturno": True,
        "cara_corazon": True
    },
    "vaquita": {
        "tipo": "individuo",
        "tiene_pelo": True,
        "da_leche": True,
        "tiene_ubres": True
    },
    "torito": {
        "tipo": "individuo",
        "tiene_pelo": True,
        "da_leche": True,
        "cuernos_grandes": True,
        "robusto": True,
        "tiene_ubres": False
    }
}

# REGLAS
def es_mamifero(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return d.get("tiene_pelo", False) or d.get("da_leche", False)

def es_ave(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return d.get("tiene_plumas", False) or (d.get("vuela", False) and d.get("pone_huevos", False))

def es_carnivoro(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_mamifero(nombre_animal) and d.get("come_carne", False)

def es_ungulado(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_mamifero(nombre_animal) and d.get("tiene_pezunas", False)

def es_guepardo(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_carnivoro(nombre_animal) and d.get("color_leonado", False) and d.get("manchas_oscuras", False)

def es_tigre(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_carnivoro(nombre_animal) and d.get("rayas_negras", False)

def es_jirafa(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_ungulado(nombre_animal) and d.get("cuello_largo", False) and d.get("manchas_oscuras", False)

def es_cebra(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_ungulado(nombre_animal) and d.get("rayas_negras", False)

def es_pinguino(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_ave(nombre_animal) and d.get("nada", False) and d.get("blanco_y_negro", False)

def es_albatros(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_ave(nombre_animal) and d.get("vuela_bien", False)

def es_buho(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_ave(nombre_animal) and d.get("es_nocturno", False) and d.get("ojos_frontales", False) and d.get("tiene_penachos", False)

def es_lechuza(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_ave(nombre_animal) and d.get("es_nocturno", False) and d.get("cara_corazon", False)

def es_vaca(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_mamifero(nombre_animal) and d.get("tiene_ubres", False)

def es_toro(nombre_animal):
    d = hechos_animales.get(nombre_animal, {})
    return es_mamifero(nombre_animal) and d.get("cuernos_grandes", False) and d.get("robusto", False) and not d.get("tiene_ubres", True)

# EJEMPLO DE PRUEBA
if __name__ == "__main__":
    print("¿Es tigrito un tigre?:", es_tigre("tigrito"))    
    print("¿Es jirafita una jirafa?:", es_jirafa("jirafita"))      
    print("¿Es buhito un buho?:", es_buho("buhito"))                 
    print("¿Es vaquita una vaca?:", es_vaca("vaquita"))          
    print("¿Es torito un toro?:", es_toro("torito"))                 
    print("¿Es un guepardito un guepardo?:", es_guepardo("guepardito"))
    print("¿Es albatrocito una cebra?:", es_cebra("albatrocito"))