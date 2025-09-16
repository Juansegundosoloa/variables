asignaturas = ["Matemática", "Física", "Química", "Historia", "Lengua"]
repetir = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 6:
        repetir.append(asignatura)

if repetir:
    print("Tienes que repetir las siguientes asignaturas:")
    print(", ".join(repetir))
else:
    print("Has aprobado todas las asignaturas")