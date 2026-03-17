from controllers.auth_controller import auth_bp

app.register_blueprint(auth_bp, url_prefix="/auth")