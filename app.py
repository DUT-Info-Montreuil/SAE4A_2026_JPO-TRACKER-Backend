from flask import Flask
from flask_cors import CORS
from config import Config
from extension import mongo
from controler.visiteur_controler import visiteur_bp
from controler.export_controler import export_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Init extensions
    mongo.init_app(app)

    
    CORS(app)

    # Register blueprints
    app.register_blueprint(visiteur_bp)
    app.register_blueprint(export_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
