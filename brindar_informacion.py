# Brindar información según la preferencia elegida
consulta = input("Ingrese su artista, película de Disney, color, comida o serie de Netflix: ").lower()
match consulta:
    case "billie eilish":
        info = "Cantante y compositora estadounidense de pop alternativo con múltiples premios Grammy."
    case "monsters university":
        info = "Película animada de Disney Pixar que muestra cómo Mike y Sulley se conocieron en la universidad."
    case "azul":
        info = "Un color primario asociado a la calma, la tranquilidad y el océano."
    case "pozole":
        info = "Platillo tradicional mexicano a base de granos de maíz nixtamalizado y carne."
    case "mushoku tensei":
        info = "Reconocida serie de anime del género isekai disponible en plataformas de streaming."
    case _:
        info = "No se encontró información."
print("Información:", info)