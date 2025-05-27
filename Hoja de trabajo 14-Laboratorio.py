#Datos
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes",]
niveles_azucar = [130, 160, 95, 175, 160]     # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700]  # mg
presion_sistolica = [115, 130, 110, 125, 175]           # mmHg
presion_diastolica = [78, 79, 85,89 , 92]           # mmHg


#Parámetros
azucar_min = 70
azucar_max = 140
sal_max = 2300

#Clasificar presion arterial
def clasificar_presion(sistonica, diastolica):
    if  sistonica>=140 or diastolica>=90:
        return"Hipertension etapa 2"
    elif 130 <=sistonica <= 139 or 80 <= diastolica<= 89:
        return "Hipertension etapa 1"
    elif 120 <= sistonica <= 129 and diastolica<80:
        return "Elevada"
    elif sistonica <120 and diastolica<80:
        return "Normal"
    else:
        return"Indefinida"

#Evaluación Diaria
# Evaluación diaria
print("Evaluación diaria:")
for i in range(len(dias)):
    alerta = []
    azucar = niveles_azucar[i]
    sal = niveles_sal[i]
    sis = presion_sistolica[i]
    dias_ = presion_diastolica[i]
    presion_cat = clasificar_presion(sis, dias_)

    if azucar < azucar_min or azucar > azucar_max:
        alerta.append("Azúcar fuera de rango")
    if sal > sal_max:
        alerta.append("Sal excedida")
    if presion_cat != "Normal":
        alerta.append(f"Presión arterial: {presion_cat}")

    print(f"{dias[i]}:")
    print(f"  Azúcar: {azucar} mg/dL")
    print(f"  Sal: {sal} mg")
    print(f"  Presión: {sis}/{dias_} mmHg ({presion_cat})")
    print(f"  Alertas: {'; '.join(alerta) if alerta else 'Todo en rango'}\n")
    
# Promedios semanales
prom_azucar = sum(niveles_azucar) / len(niveles_azucar)
prom_sal = sum(niveles_sal) / len(niveles_sal)
prom_sis = sum(presion_sistolica) / len(presion_sistolica)
prom_dias = sum(presion_diastolica) / len(presion_diastolica)
presion_prom_cat = clasificar_presion(prom_sis, prom_dias)

print("Resumen semanal:")
print(f"  Promedio azúcar: {prom_azucar:.1f} mg/dL {'❗' if prom_azucar > azucar_max else ''}")
print(f"  Promedio sal: {prom_sal:.1f} mg {'❗' if prom_sal > sal_max else ''}")
print(f"  Promedio presión: {prom_sis:.1f}/{prom_dias:.1f} mmHg ({presion_prom_cat})")
