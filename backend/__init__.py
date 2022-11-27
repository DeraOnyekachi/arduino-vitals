from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def create_app():
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app

app = create_app()

if __name__ == "__main__":
    app.run()