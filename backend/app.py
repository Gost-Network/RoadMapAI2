from flask import Flask, render_template
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

template_dir = os.path.join(
    BASE_DIR,
    "..",
    "frontend",
    "templates"
)

static_dir = os.path.join(
    BASE_DIR,
    "..",
    "frontend",
    "static"
)

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir
)

from backend.routes.search_routes import search_bp
from backend.routes.route_routes import route_bp
from backend.routes.safety_routes import safety_bp

app.register_blueprint(search_bp)
app.register_blueprint(route_bp)
app.register_blueprint(safety_bp)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/health")
def health():
    return {
        "status": "running",
        "project": "Road Map AI"
    }
print("BASE_DIR =", BASE_DIR)
print("TEMPLATE_DIR =", template_dir)
print("STATIC_DIR =", static_dir)