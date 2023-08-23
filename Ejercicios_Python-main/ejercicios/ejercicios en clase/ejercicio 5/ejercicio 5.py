
from data import heroes_info

for super_heroe in heroes_info:
    print(f" \nID: {super_heroe ['ID']},  Codername: {super_heroe['Nombre']} ")
    print(f"Identidad: {super_heroe['Identidad']}, Origen: {super_heroe['Origen']}")
    habilidades = set(super_heroe['Habilidades'])
    print(f"Habilidades: {habilidades}")
    print("--------------------------------------------------------------------------")