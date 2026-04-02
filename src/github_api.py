import json
import urllib.request
import urllib.error


def fetch_user_activity(username):
    """
    Obtiene la actividad reciente de un usuario de GitHub.
    
    Args:
        username (str): Nombre de usuario de GitHub.
    
    Returns:
        list: Lista de eventos del usuario.
    
    Raises:
        ValueError: Si el usuario no existe.
        ConnectionError: Si ocurre un problema al conectar con la API.
        Exception: Para otros errores inesperados.
    """
    url = f"https://api.github.com/users/{username}/events"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Python-GitHub-Activity-App"}
        )

        with urllib.request.urlopen(request) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)

    except urllib.error.HTTPError as error:
        if error.code == 404:
            raise ValueError("El usuario no existe en GitHub.")
        raise Exception(f"Error HTTP: {error.code}")

    except urllib.error.URLError:
        raise ConnectionError("No fue posible conectar con la API de GitHub.")

    except json.JSONDecodeError:
        raise Exception("La respuesta de la API no pudo ser interpretada como JSON.")