universo = {
    "Estudiantes": {
        "Abraham": {
            "Materias": ["Programacion", "TallerDeInvestigacion"],
            "Grupo": ["7SF"]
        },
        "Miguel": {
            "Materias": ["Programacion", "TallerDeInvestigacion"],
            "Grupo": ["7SE"]
        },
        "Alejandra": {
            "Materias": ["Programacion", "TallerDeInvestigacion"],
            "Grupo": ["7SE"]
        }
    },
    "Profesores": {
        "Prof.Juan": ["TallerDeInvestigacion"],
        "Profra.Maria": ["Programacion"]
    },
    "Edificios": {
        "Cafeteria": {
            "Zona": ["ZonaNorte"],
            "Uso": ["Comer"]
        },
        "SalonDeConferencia": {
            "Zona": ["ZonaSur"],
            "Uso": ["Charlas"]
        },
        "Cancha": {
            "Zona": ["ZonaNorte"],
            "Uso": ["Deportes"]
        }
    },
    "Trabajadores": {
        "Profesor": ["Enseñar"],
        "Guardia": ["Revisar"],
        "Administrador": ["Administrar"]
    }
}

#1 Estudiante
def Estudiante(x): 
    for estudiante, datos in universo["Estudiantes"].items():
        if estudiante == x: 
            return True
    return False

#2 Profesor 
def Profesor(y): 
    for profesor, materias in universo["Profesores"].items():
        if profesor == y: 
            return True
    return False 

#3 Materias 
def Materia(m): 
    for estudiante, datos in universo["Estudiantes"].items(): 
        for materia in datos["Materias"]:
            if materia == m: 
                return True
    return False

#4 DaMateria
def DaMateria(y, m): 
    for profesor, materias in universo["Profesores"].items():
        if profesor == y: 
            for materia in materias: 
                if materia == m: 
                    return True
    return False

#5 MismoGrupo
def MismoGrupo(x, y): 
    for estudiante1, datos1 in universo["Estudiantes"].items(): 
        if estudiante1 == x: 
            for estudiante2, datos2 in universo["Estudiantes"].items():
                if estudiante2 == y: 
                    if datos1["Grupo"] == datos2["Grupo"]: 
                        return True
    return False

#6 UsoEdificio 
def UsoEdificio(e, u):
    for edificio, datos in universo["Edificios"].items():
        if edificio == e:
            for uso in datos["Uso"]:
                if uso == u:
                    return True
    return False

#7 FuncionTrabajador 
def FuncionTrabajador(t, a):
    for trabajador, funciones in universo["Trabajadores"].items():
        if trabajador == t:
            for funcion in funciones:
                if funcion == a:
                    return True
    return False

print("\n#1")
print("Positivo:", Estudiante("Abraham"))
print("Negativo:", Estudiante("Prof.Juan"))

print("\n#2")
print("Positivo:", Profesor("Profra.Maria"))
print("Negativo:", Profesor("Alejandra"))

print("\n#3")
print("Positivo:", Materia("Programacion"))
print("Negativo:", Materia("7SF"))

print("\n#4")
print("Positivo:", DaMateria("Prof.Juan", "TallerDeInvestigacion"))
print("Negativo:", DaMateria("Profra.Maria", "TallerDeInvestigacion"))

print("\n#5")
print("Positivo:", MismoGrupo("Miguel", "Alejandra"))
print("Negativo:", MismoGrupo("Miguel", "Abraham"))

print("\n#6")
print("Positivo:", UsoEdificio("Cafeteria", "Comer"))
print("Negativo:", UsoEdificio("Cancha", "Charlas"))

print("\n#7")
print("Positivo:", FuncionTrabajador("Guardia", "Revisar"))
print("Negativo:", FuncionTrabajador("Administrador", "Enseñar"))