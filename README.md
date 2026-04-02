https://roadmap.sh/projects/github-user-activity

# 🚀 GitHub User Activity CLI

Una aplicación de línea de comandos (CLI) desarrollada en Python que permite obtener y mostrar la actividad reciente de un usuario de GitHub utilizando la API pública de GitHub.

---

## 📌 Descripción del Proyecto

Este proyecto consiste en una herramienta tipo CLI orientada a backend que permite:

* Consultar la actividad pública reciente de cualquier usuario de GitHub
* Procesar datos en formato JSON provenientes de la API
* Mostrar la información de manera legible en la terminal

Fue desarrollado como práctica para fortalecer habilidades en:

* Consumo de APIs REST
* Manejo de datos JSON
* Desarrollo de aplicaciones CLI
* Manejo de errores y robustez en backend

---

## 🧠 Funcionalidades principales

* 🔍 Consulta de actividad de usuarios mediante API de GitHub
* 💻 Interacción desde la línea de comandos
* 🧾 Salida formateada y fácil de leer
* ⚠️ Manejo adecuado de errores (usuario inválido, fallas de API, etc.)
* 🚫 Implementado sin librerías externas (solo librerías estándar de Python)

---

## 🛠️ Tecnologías utilizadas

* Python 3.x
* `urllib` → para realizar solicitudes HTTP
* `json` → para procesar la respuesta de la API
* `sys` → para manejar argumentos desde la terminal

---

## 📂 Estructura del proyecto

```"
github-user-activity/
│
├── main.py
├── README.md
├── .gitignore
└── src/
    ├── __init__.py
    ├── github_api.py
    └── formatter.py
```

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```"
git clone https://github.com/cristotest/github-user-activity.git
cd github-user-activity
```

### 2. Crear un entorno virtual

```"
python -m venv venv
```

### 3. Activar el entorno virtual

#### Windows (PowerShell)

```"
venv\Scripts\Activate
```

#### Mac/Linux

```"
source venv/bin/activate
```

---

## ▶️ Uso

Ejecuta la aplicación desde la terminal:

```"
python main.py <nombre_usuario_github>
```

### Ejemplo:

```"
python main.py octocat
```

---

## 📊 Ejemplo de salida

```"
Actividad reciente de GitHub para: octocat

- Pushed 2 commit(s) to octocat/Hello-World
- Starred octocat/Spoon-Knife
- Opened a pull request in octocat/test-repo
```

---

## ⚠️ Manejo de errores

La aplicación contempla los siguientes escenarios:

* ❌ Usuario no existente
* 🌐 Errores de conexión con la API
* ⚡ Errores inesperados en ejecución

Ejemplo:

```"
Error: El usuario no existe en GitHub.
```

---

## 🚀 Mejoras futuras

* Filtrar actividad por tipo de evento (commits, issues, PRs)
* Implementar argumentos avanzados con `argparse`
* Agregar pruebas unitarias
* Implementar caché para optimizar rendimiento
* Soporte para paginación de resultados
* Salida con colores en terminal

---

## 🎯 Aprendizajes obtenidos

Durante este proyecto se fortalecieron habilidades en:

* Desarrollo de herramientas CLI en Python
* Consumo de APIs REST
* Manejo de estructuras JSON
* Organización de código modular
* Manejo adecuado de errores en aplicaciones backend

---

## 👨‍💻 Autor

🔗 GitHub: https://github.com/cristotest

---

