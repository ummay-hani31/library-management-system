from flask import Flask, redirect
from config import Config
from models import db, Admin
from flask_login import LoginManager

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.books import books_bp
from routes.students import students_bp
from routes.categories import categories_bp
from routes.transactions import transactions_bp
from routes.reports import reports_bp

login_manager = LoginManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(reports_bp)

    @app.route("/")
    def home():
        return redirect("/login")

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    with app.app_context():

        db.create_all()

        admin = Admin.query.filter_by(username="admin").first()

        if not admin:
            admin = Admin(username="admin")
            admin.set_password("admin123")

            db.session.add(admin)
            db.session.commit()

            print("--------------------------------")
            print("Default Admin Created")
            print("Username : admin")
            print("Password : admin123")
            print("--------------------------------")

    return app


app = create_app()

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)