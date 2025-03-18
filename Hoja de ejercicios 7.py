#1.	Escribe un programa que extraiga la primera y la última palabra de una oración. Split()
def primera_ultima_palabra(oracion):
    palabras = oracion.split()
    return f"Primera palabra: {palabras[0]}, Última palabra: {palabras[-1]}"

entrada = "Python es un lenguaje poderoso y versátil"
print(primera_ultima_palabra(entrada))

#2.	Crea un programa que elimine los espacios repetidos en una cadena
def limpiar_espacio(texto):
    return " ".join(texto.split())
entrada = "Hola     mundo              en                python"
print(limpiar_espacio(entrada))


#3.	Dado un correo electrónico, extrae solo el dominio.
def extraer_dominio(email):
    return email.split('@')[-1]
entrada = "usuario@gmail.com"
print(extraer_dominio(entrada))

#4.	Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf).
def verificar_extension(nombre_archico, extension=".pdf"):
    return nombre_archico.endswith(extension)
print(verificar_extension("documento.pdf"))
print(verificar_extension("imagen.jpg"))

#5.	Dado un texto, invierte el orden de las palabras
def invertir_palabras(texto):
    return " ".join(texto.split()[ ::-1])
entrada = "Me gusta Python"
print(invertir_palabras(entrada))

#6.	Dado un texto ingresado por el usuario detectar palabras claves y responder:
def responder_texto(texto):
    respuesta = {
        "poma": """Podrá nublarse el sol eternamente;
Podrá secarse en un instante el mar;
Podrá romperse el eje de la tierra
Como un débil cristal""",
"Cancion": """Eres como la noche, callada y constelada.
Tu silencio es de estrella, tan lejano y sencillo.
Me gustas cuando callas porque estás como ausente.
Distante y dolorosa como si hubieras muerto."""
                }

 for clave in respuestas:
        if clave in texto.lower():
            return respuestas[clave]
    
    return "No tengo una respuesta para eso."

entrada = "necesito que me escribas un poema de amor."
print(responder_texto(entrada))