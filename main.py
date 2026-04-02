import sys
from src.github_api import fetch_user_activity
from src.formatter import format_events


def main():
    """
    Función principal del programa.
    """
    if len(sys.argv) != 2:
        print("Uso: python main.py <github_username>")
        sys.exit(1)

    username = sys.argv[1].strip()

    if not username:
        print("Error: Debes proporcionar un nombre de usuario válido.")
        sys.exit(1)

    try:
        events = fetch_user_activity(username)
        formatted_events = format_events(events)

        print(f"\nActividad reciente de GitHub para: {username}\n")
        for event in formatted_events:
            print(event)

    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

    except ConnectionError as error:
        print(f"Error de conexión: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()