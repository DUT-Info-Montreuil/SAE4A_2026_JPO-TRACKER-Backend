from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from config import Config
from extension import mongo
from controler.visiteur_controler import visiteur_bp
from controler.export_controler import export_bp
from flask_cors import CORS
from controler.auth_controler import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    mongo.init_app(app)

    app.register_blueprint(export_bp)
    app.register_blueprint(visiteur_bp)
    app.register_blueprint(auth_bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run()