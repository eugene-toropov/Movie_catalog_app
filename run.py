from project.config import config
from project.server import create_app
from project.setup.db import db

app = create_app(config)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(port=25000)
