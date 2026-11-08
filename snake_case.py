import re
import unicodedata


def to_snake_case(texto: str) -> str:
    # Eliminar tildes
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    # Convertir a minúsculas
    texto = texto.lower()

    # Reemplazar espacios y caracteres especiales por _
    texto = re.sub(r"[^a-z0-9]+", "_", texto)

    # Eliminar _ al inicio y al final
    texto = texto.strip("_")

    return texto


def main():
    print("=== CONVERSOR A SNAKE_CASE ===")

    while True:
        texto = input("\nIngresa el texto que deseas convertir (o escribe 'salir' para terminar): ")

        if texto.strip().lower() == "salir":
            print("¡Hasta luego!")
            break

        if not texto.strip():
            print("Por favor, ingresa un texto válido.")
            continue

        resultado = to_snake_case(texto)

        print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()