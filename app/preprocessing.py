import re
import string

# função responsável por normalizar os textos
def preprocessarTexto(texto):
    # Remove pontuações
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    # Converte para minúsculas
    texto = texto.lower()
    # Remove números
    texto = re.sub(r'\d+', '', texto)
    # Remove espaços em branco extras
    texto = texto.strip()
    return texto
