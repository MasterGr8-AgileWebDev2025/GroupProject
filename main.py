from app import DeploymentConfig, create_application, db
from flask_migrate import Migrate

if __name__ == "__main__":
    app = create_application(DeploymentConfig)
    migrate = Migrate(app, db)
    app.run(host="0.0.0.0", port=5000, debug=True)
