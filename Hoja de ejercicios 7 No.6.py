def responder_texto(texto):
    respuestas = {
        "poema": """Podrá nublarse el sol eternamente;
Podrá secarse en un instante el mar;
Podrá romperse el eje de la tierra
Como un débil cristal.""",
        "canción": """Eres como la noche, callada y constelada.
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