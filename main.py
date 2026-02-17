from flask import Flask, render_template

app = Flask(__name__)

# =============================
# Datos del portafolio
# Agrega/editas proyectos aquí. Cada proyecto debe incluir:
#  - slug: identificador único (string sin espacios)
#  - title: título del proyecto
#  - description: breve descripción (1-2 oraciones)
#  - image: ruta relativa dentro de static (por ejemplo, 'img/python-project.png')
#  - tags: lista de tecnologías
#  - github_url: enlace al repositorio
# =============================
projects = [
    {
        "slug": "api-rest-flask-sqlite",
        "title": "API REST con Flask y SQLite",
        "description": "API ligera para operaciones CRUD sobre SQLite con endpoints organizados y buenas prácticas básicas.",
        "image": "img/python-project.png",
        "tags": ["Python", "Flask", "SQLite"],
        "github_url": "https://github.com/novxKodland12/ambiental_calc_v1.2.0.git",
    },
    {
        "slug": "discord-bot-moderacion",
        "title": "Bot de Discord para Moderación",
        "description": "Bot modular para Discord con comandos de moderación, roles y logging de eventos.",
        "image": "img/discord.png",
        "tags": ["Python", "Discord Bots"],
        "github_url": "hhttps://github.com/novxKodland12/bot_anticontaminacion",
    },
    {
        "slug": "landing-estatica-html-css",
        "title": "Landing Estática HTML/CSS",
        "description": "Sitio estático responsive con buenas prácticas de semántica, accesibilidad y performance.",
        "image": "img/html.png",
        "tags": ["HTML", "CSS"],
        "github_url": "https://github.com/novxKodland12/widget_weather_v1.0.9.git",
    },
    {
        "slug": "reportes-sqlite-visualizacion",
        "title": "Reportes y Visualización con SQLite",
        "description": "Extracción de datos desde SQLite y generación de reportes con visualización ligera.",
        "image": "img/db.webp",
        "tags": ["Python", "SQLite"],
        "github_url": "https://github.com/novxKodland12/bloc_Notas_v1.1.0.git",
    },
]


@app.route("/")
def index():
    # Renderiza la plantilla principal y pasa la lista de proyectos
    return render_template("index.html", projects=projects)


if __name__ == "__main__":
    # Ejecuta la app en modo desarrollo
    app.run(debug=True)
