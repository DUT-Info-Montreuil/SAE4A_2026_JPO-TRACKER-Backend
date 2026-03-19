from flask import Flask
from config import Config
from extension import mongo
from controler.visiteur_controler import visiteur_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    mongo.init_app(app)

    # Register blueprints
    app.register_blueprint(visiteur_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
