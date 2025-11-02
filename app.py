from flask import Flask
from flask_cors import CORS
from config.database import engine, Base
from models.menu_model import Menus
from routes.web import web
import os 

# insialisasi app
app = Flask(__name__)
cors = CORS(app)

# Buat tabel otomatis kalau belum ada
Base.metadata.create_all(bind=engine)

# Daftarkan blueprint routes
app.register_blueprint(web)

# Hanya untuk testing lokal(railway akan jalankan lewat Gunicorn)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
