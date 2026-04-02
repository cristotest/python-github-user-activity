def format_event(event):
    """
    Convierte un evento de GitHub en un mensaje legible.
    
    Args:
        event (dict): Evento individual obtenido desde la API.
    
    Returns:
        str: Mensaje formateado.
    """
    event_type = event.get("type", "UnknownEvent")
    repo_name = event.get("repo", {}).get("name", "repositorio desconocido")
    payload = event.get("payload", {})

    if event_type == "PushEvent":
        commit_count = len(payload.get("commits", []))
        return f"Pushed {commit_count} commit(s) to {repo_name}"

    if event_type == "IssuesEvent":
        action = payload.get("action", "performed an action on")
        return f"{action.capitalize()} an issue in {repo_name}"

    if event_type == "WatchEvent":
        return f"Starred {repo_name}"

    if event_type == "ForkEvent":
        return f"Forked {repo_name}"

    if event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "resource")
        return f"Created a new {ref_type} in {repo_name}"

    if event_type == "DeleteEvent":
        ref_type = payload.get("ref_type", "resource")
        return f"Deleted a {ref_type} in {repo_name}"

    if event_type == "PullRequestEvent":
        action = payload.get("action", "performed an action on")
        return f"{action.capitalize()} a pull request in {repo_name}"

    return f"Performed {event_type} in {repo_name}"


def format_events(events):
    """
    Convierte una lista de eventos en una lista de mensajes.
    
    Args:
        events (list): Lista de eventos.
    
    Returns:
        list: Lista de strings formateados.
    """
    if not events:
        return ["No se encontró actividad reciente para este usuario."]

    return [f"- {format_event(event)}" for event in events]